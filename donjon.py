import random

class Monstre:
    def __init__(self, nom, pv, force):
        self.nom = nom
        self.pv = pv
        self.force = force

class Salle:
    def __init__(self):
        self.monstre = None
        self.tresor = None
        self.connexions = {}

    def connecter(self, direction, autre_salle):
        self.connexions[direction] = autre_salle

    def __str__(self):
        contenu = []
        if self.monstre:
            contenu.append(f"Monstre: {self.monstre.nom}")
        if self.tresor:
            contenu.append(f"Trésor: {self.tresor}")
        if not contenu:
            contenu.append("La salle est vide.")
        return ", ".join(contenu)

class Donjon:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.salles = [[Salle() for _ in range(hauteur)] for _ in range(largeur)]
        self.generer_connexions()
        self.position_joueur = (0, 0)
        self.initialiser_salles()

    def generer_connexions(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                if x > 0:
                    self.salles[x][y].connecter("ouest", self.salles[x-1][y])
                if x < self.largeur - 1:
                    self.salles[x][y].connecter("est", self.salles[x+1][y])
                if y > 0:
                    self.salles[x][y].connecter("nord", self.salles[x][y-1])
                if y < self.hauteur - 1:
                    self.salles[x][y].connecter("sud", self.salles[x][y+1])

    def initialiser_salles(self):
        for x in range(self.largeur):
            for y in range(self.hauteur):
                if random.random() < 0.2:  # 20% 
                    self.salles[x][y].monstre = Monstre("Gobelin", 20, 5)
                if random.random() < 0.1:  # 10% 
                    self.salles[x][y].tresor = "Or"

    def obtenir_salle(self, x, y):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.salles[x][y]
        return None

    def deplacer_joueur(self, direction):
        x, y = self.position_joueur
        nouvelle_position = (x, y)
        if direction in self.salles[x][y].connexions:
            nouvelle_salle = self.salles[x][y].connexions[direction]
            for idx_x, ligne in enumerate(self.salles):
                for idx_y, salle in enumerate(ligne):
                    if salle == nouvelle_salle:
                        nouvelle_position = (idx_x, idx_y)
                        break
        self.position_joueur = nouvelle_position
        return self.position_joueur

    def afficher_salle_actuelle(self):
        x, y = self.position_joueur
        salle_actuelle = self.obtenir_salle(x, y)
        return str(salle_actuelle)

def creer_donjon(largeur, hauteur):
    return Donjon(largeur, hauteur)
