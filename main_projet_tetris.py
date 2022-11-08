'''
Programme Tetris L1 BN EFREI
'''


path = input("Spécifier le chemin d'accès : ")


programme = open(path, "w")
#"C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt"



class Grille:
    
    def __init__(self) -> None:
        self.nb_colonne = 21
        self.grille = []
        self.lst_lettre_maj = []
        self.lst_lettre_min = []

    def create_grid(self):
        grille_2 = []
        for i in range(self.nb_colonne):
            for j in range(self.nb_colonne):
                grille_2.append(0)
            self.grille.append(grille_2)
            grille_2 = []
        return self.grille
    
    def read_grid(self):
        programme.write('  ')
        for k in range(len(self.lst_lettre_min)):
            programme.write(self.lst_lettre_min[k])
        programme.write('\n')
        for i in range(21):
            programme.write(self.lst_lettre_maj[i])
            programme.write(' ')
            for j in range(len(self.grille[i])):
                programme.write(str(self.grille[i][j]))
            programme.write("\n")

    
    #Affichage des lettres
    def lettre_min(self):
        for i in range(97, 118):
            lettre_min = chr(i)
            self.lst_lettre_min.append(lettre_min)
        #print(self.lst_lettre_min, len(self.lst_lettre_min))

    def lettre_maj(self):
        for i in range(65, 86):
            lettre_maj = chr(i)
            self.lst_lettre_maj.append(lettre_maj)
        #print(self.lst_lettre_maj, len(self.lst_lettre_maj))
    #Fin Affichage des Lettres
    






'''
class Figures:

    def __init__(self) -> None:
        self.a = 5
    
    #def figures_cercles(self):

class Regle_du_jeu:
    def __init__(self) -> None:
        pass           
    
    def affichage(self):
        print("Commmencer à jouer")
        print("Afficher les réglages du jeu")
'''








if __name__ == "__main__":
    gg = Grille()
    gg.lettre_min()
    gg.lettre_maj()


    gg.create_grid()
    gg.read_grid()

    

    
