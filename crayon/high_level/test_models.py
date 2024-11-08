from django.test import TestCase
from .models import Ville, Usine, Machine, Stock, Ressource, Recette, RecetteIngredient

class UsineTests(TestCase):
    def setUp(self):
        ville = Ville.objects.create(nom="Labège", code_postal="31400", prix_m2=2000)
        self.usine = Usine.objects.create(nom="Usine 1", surface=50, ville=ville)
        machine1 = Machine.objects.create(nom="Machine A", prix=1000, n_serie="12345")
        machine2 = Machine.objects.create(nom="Machine B", prix=2000, n_serie="67890")
        self.usine.machines.set([machine1, machine2])
        ressource = Ressource.objects.create(nom="Bois", prix=10)
        Stock.objects.create(ressource=ressource, nombre=1000)
    
    def test_costs(self):
        expected_cost = 110750
        self.assertEqual(self.usine.costs(), expected_cost)

