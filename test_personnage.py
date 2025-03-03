import unittest
from personnage import creation_personnage

class TestPersonnage(unittest.TestCase):

    def test_creation_personnage_valide(self):
        perso = creation_personnage("Mohamed", "guerrier")
        self.assertEqual(perso.nom, "Mohamed")
        self.assertEqual(perso.classe, "guerrier")
        self.assertEqual(perso.pv, 150)
        self.assertEqual(perso.pm, 50)
        self.assertEqual(perso.force, 15)

    def test_validation_nom_trop_court(self):
        with self.assertRaises(ValueError):
            creation_personnage("", "mage")

    def test_validation_nom_trop_long(self):
        with self.assertRaises(ValueError):
            creation_personnage("a" * 21, "voleur")

    def test_selection_classe_valide(self):
        perso = creation_personnage("Samy", "mage")
        self.assertEqual(perso.classe, "mage")
        self.assertEqual(perso.intelligence, 15)

    def test_affichage_recapitulatif(self):
        perso = creation_personnage("Legolas", "voleur")
        recap = str(perso)
        self.assertIn("Personnage: Legolas", recap)
        self.assertIn("Classe: voleur", recap)
        self.assertIn("Points de Vie (PV): 110", recap)

if __name__ == '__main__':
    unittest.main()
