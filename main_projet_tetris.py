'''
Programme Tetris L1 BN EFREI
'''

class Grille:
    
    def __init__(self) -> None:
        self.nb_colonne = 21

    def grille(self):

        self.grille_principale = []
        self.grille_secondaire = []

        for i in range(self.nb_colonne):
            for j in range(self.nb_colonne):
                self.grille_secondaire.append(0)
            self.grille_principale.append(self.grille_secondaire)

    def affichage_grille(self):
        for k in range(len(self.grille_principale)):
            for l in range(len(self.grille_principale[k])):
                programme.write(str(self.grille_principale[k][l]))
            programme.write("\n")
            
print("Commmencer à jouer")
print("Afficher les réglages du jeu")

if __name__ == "__main__":
    gg = Grille()

    gg.grille()
    gg.affichage_grille()
    
