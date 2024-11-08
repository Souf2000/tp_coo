from high_level.models import Ville, Machine, Produit

# Ajouter une nouvelle ville
ville1 = Ville(nom="Toulouse", code_postal="31000", prix_m2=200.00)
ville1.save()

# Ajouter une nouvelle machine
machine1 = Machine(nom="Machine A", prix=15000.00, n_serie="S12345")
machine1.save()

# Ajouter un nouveau produit
produit1 = Produit(nom="Produit X", prix=25.00, premiere_etape=None)  # Remplace None par une instance d'étape si nécessaire
produit1.save()
