'''
Programme Tetris L1 BN EFREI
'''


#path = input("Spécifier le chemin d'accès : ")


programme = open("C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt", "w")
#"C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt"



class Grille:
    
    def __init__(self) -> None:
        self.nb_colonne = 21
        self.grille = []
        self.lst_lettre_maj = []
        self.lst_lettre_min = []

    def create_grid(self, chiffre_donné):
        grille_2 = []
        for i in range(self.nb_colonne):
            for j in range(self.nb_colonne):
                chiffre = str(chiffre_donné)+"  "
                grille_2.append(chiffre)
            self.grille.append(grille_2)
            grille_2 = []
        return self.grille
    
    def read_grid(self):
        programme.write('   ')
        for k in range(len(self.lst_lettre_min)):
            programme.write(self.lst_lettre_min[k])
        programme.write('\n')
        for i in range(21):
            programme.write(self.lst_lettre_maj[i])
            for j in range(len(self.grille[i])):
                programme.write(str(self.grille[i][j]))
            programme.write("\n")

    
    #Affichage des lettres
    def lettre_min(self):
        for i in range(97, 118):
            lettre_min = chr(i)
            lettre = lettre_min + '  '
            self.lst_lettre_min.append(lettre)
        #print(self.lst_lettre_min, len(self.lst_lettre_min))

    def lettre_maj(self):
        for i in range(65, 86):
            lettre_maj = chr(i)
            lettre = lettre_maj + '  '
            self.lst_lettre_maj.append(lettre)
        #print(self.lst_lettre_maj, len(self.lst_lettre_maj))
    #FIn Affichage des Lettres
    
    #Figures
    def figure_triangle(self):
        min = 10
        max = 11
        for i in range(11):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min -= 1
            max += 1

    def figure_losange(self):
        min = 10
        max = 11
        for i in range(11):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min -= 1
            max += 1
        min = 0
        max = 21
        for i in range(10,20):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min += 1
            max -= 1
        self.grille[20][10] = '1  '
    
    def figure_cercle(self, trou):
        #Haut Gauche
        max = 5
        min = 0
        for i in range(5):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            max-=1
        #Haut Droit
        max = 21
        min = 16
        for i in range(5):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            min+=1
        #Bas Gauche
        max = 5
        min = 1
        for i in range(16,21):
            for j in range(min):
                self.grille[i][j] = str(trou)+'  '
            min+=1
        #Bas Droit
        max = 21
        min = 21
        for i in range(15,21):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            min-=1
    #Fin Figures




class Regle_du_jeu:
    def __init__(self) -> None:
        pass
    
    def affichage(self):
        print("1 - Commmencer à jouer")
        print("2 - Afficher les réglages du jeu")
        self.choice_user = int(input("Faire votre choix : "))
        while self.choice_user<1 or self.choice_user>2:
            self.choice_user = int(input("Faire votre choix : "))

        if self.choice_user == 1:
            print("Choississez votre plateau de jeu :")
            print("1 - Triangle")
            print("2 - Losange")
            print("3 - Cercle")
            self.choice_user_plateau = int(input("Faire votre choix : "))
            while self.choice_user_plateau<1 or self.choice_user_plateau>3:
                self.choice_user_plateau = int(input("Faire votre choix : "))
            
            if self.choice_user_plateau == 1:
                Grille.create_grid(0)
                Grille.lettre_min()
                Grille.lettre_maj()
                Grille.figure_triangle()
                Grille.read_grid()
            if self.choice_user_plateau == 2:
                Grille.create_grid(0)
                Grille.lettre_min()
                Grille.lettre_maj()
                Grille.figure_losange()
                Grille.read_grid()
            if self.choice_user_plateau == 1:
                Grille.create_grid(1)
                Grille.lettre_min()
                Grille.lettre_maj()
                Grille.figure_cercle(' ')
                Grille.read_grid()











if __name__ == "__main__":
    
    rr = Regle_du_jeu()
    rr.affichage()

    

    

    

    

    
