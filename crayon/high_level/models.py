from django.db import models
from decimal import Decimal

# Classe Objet (classe de base pour les objets ayant un nom et un prix)
class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": str(self.prix),  # Convertir en string pour la sérialisation JSON
        }

# Classe Ville
class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    prix_m2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_m2": str(self.prix_m2),
        }

# Classe Ressource (hérite d'Objet)
class Ressource(Objet):
    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": str(self.prix),
        }

# Classe Local (classe abstraite)
class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT)  # Relation de composition avec Ville
    surface = models.IntegerField()

    class Meta:
        abstract = True

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "ville": self.ville.json(),
            "surface": self.surface,
        }

# Classe SiegeSocial (hérite de Local)
class SiegeSocial(Local):
    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "ville": self.ville.json(),
            "surface": self.surface,
        }

# Classe Machine (hérite d'Objet)
class Machine(Objet):
    n_serie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} (S/N: {self.n_serie})"

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": str(self.prix),
            "n_serie": self.n_serie,
        }

# Classe Usine (hérite de Local et a une relation d'agrégation avec Machine)
class Usine(Local):
    machines = models.ManyToManyField(Machine)  # Agrégation avec Machine

    def costs(self):
        ville_cost = self.ville.prix_m2 * self.surface
        machines_cost = sum(machine.prix for machine in self.machines.all())
        stock_cost = sum(stock.nombre * stock.ressource.prix for stock in Stock.objects.filter(ressource__in=[ressource for ressource in Ressource.objects.all()]))


        return ville_cost + machines_cost + stock_cost

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "ville": self.ville.json(),
            "surface": self.surface,
            "machines": [machine.json() for machine in self.machines.all()],
        }

# Classe Stock (agrégation avec Ressource)
class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.PROTECT)  # Agrégation avec Ressource
    nombre = models.IntegerField()

    def __str__(self):
        return f"{self.ressource.nom} - {self.nombre}"

    def json(self):
        return {
            "id": self.id,
            "ressource": self.ressource.json(),
            "nombre": self.nombre,
        }

# Classe QuantiteRessource (relation de composition avec Ressource)
class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.PROTECT)  # Composition avec Ressource
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ressource.nom} - {self.quantite}"

    def json(self):
        return {
            "id": self.id,
            "ressource": self.ressource.json(),
            "quantite": str(self.quantite),
        }

# Classe Etape (relation de composition avec Machine, QuantiteRessource et elle-même pour etape_suivante)
class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)  # Composition avec Machine
    quantite_ressource = models.ManyToManyField(QuantiteRessource)  # Composition avec QuantiteRessource
    duree = models.DurationField()  # Durée de l'étape
    etape_suivante = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)  # Composition avec elle-même

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "machine": self.machine.json(),
            "quantite_ressource": [qr.json() for qr in self.quantite_ressource.all()],
            "duree": str(self.duree),
            "etape_suivante": self.etape_suivante.json() if self.etape_suivante else None,
        }

# Classe Produit (composition avec Etape)
class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.PROTECT)  # Composition avec Etape

    def __str__(self):
        return f"{self.nom} - Première étape : {self.premiere_etape.nom}"

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": str(self.prix),
            "premiere_etape": self.premiere_etape.json(),
        }

# Classe Recette
class Recette(models.Model):
    nom = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ressource, through='RecetteIngredient')

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "ingredients": [ingredient.json() for ingredient in self.ingredients.all()],
        }

# Classe RecetteIngredient
class RecetteIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

    def json(self):
        return {
            "id": self.id,
            "recette": self.recette.json(),
            "ressource": self.ressource.json(),
            "quantite": str(self.quantite),
        }

# Fonction pour acheter des stocks
def acheter_stocks(usine, recette):
    for ingredient in recette.recetteingredient_set.all():
        # Vérifier le stock actuel
        stock = Stock.objects.filter(ressource=ingredient.ressource).first()
        if stock:
            # Si le stock est insuffisant, acheter plus
            if stock.nombre < ingredient.quantite:
                quantite_a_acheter = ingredient.quantite - stock.nombre
                # Simuler l'ajout de stock
                stock.nombre += quantite_a_acheter
                stock.save()
        else:
            # Si aucun stock, acheter la quantité nécessaire
            Stock.objects.create(ressource=ingredient.ressource, nombre=ingredient.quantite)
# test
