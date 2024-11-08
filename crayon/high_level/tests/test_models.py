class VilleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Cette méthode est appelée une seule fois pour toute la classe.
        cls.ville = Ville.objects.create(nom="Toulouse", code_postal="31000", prix_m2=200.00)

    def test_ville_nom(self):
        # Test pour vérifier le nom de la ville
        self.assertEqual(self.ville.nom, "Toulouse")

    def test_ville_code_postal(self):
        # Test pour vérifier le code postal de la ville
        self.assertEqual(self.ville.code_postal, "31000")
class MachineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crée une machine pour les tests
        cls.machine = Machine.objects.create(nom="Machine A", prix=15000.00, n_serie="S12345")

    def test_machine_nom(self):
        self.assertEqual(self.machine.nom, "Machine A")

    def test_machine_prix(self):
        self.assertEqual(self.machine.prix, 15000.00)

