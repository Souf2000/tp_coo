from django.test import TestCase
from high_level.models import Usine, Recette, Ressource, Stock, RecetteIngredient, Ville, Machine
from high_level.models import acheter_stocks  # Importer la fonction acheter_stocks

class UsineTests(TestCase):
    def setUp(self):
        self.ville = Ville.objects.create(nom="Labège", code_postal="31400", prix_m2=2000)
        self.usine = Usine.objects.create(nom="Usine 1", surface=50, ville=self.ville)
        self.machine = Machine.objects.create(nom="Machine A", prix=1000, n_serie="M123")
        self.usine.machines.add(self.machine)
        self.ressource1 = Ressource.objects.create(nom="Bois", prix=10)
        self.ressource2 = Ressource.objects.create(nom="Mine", prix=15)
        Stock.objects.create(ressource=self.ressource1, nombre=1000)
        Stock.objects.create(ressource=self.ressource2, nombre=50)

        self.recette = Recette.objects.create(nom="Recette 1")
        RecetteIngredient.objects.create(recette=self.recette, ressource=self.ressource1, quantite=100)
        RecetteIngredient.objects.create(recette=self.recette, ressource=self.ressource2, quantite=50)

    def test_acheter_stocks(self):
        acheter_stocks(self.usine, self.recette)
        # Ajoute des assertions ici pour vérifier les stocks après l'achat
