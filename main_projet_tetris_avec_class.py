import random as rd
import time as tm

'''
Programme Tetris L1 BN EFREI
'''

class Grille:

    def __init__(self):
        self.grille = []
        self.lst_lettre_maj = []
        self.lst_lettre_min = []

    def create_grid(self, chiffre_donné, taille):
        grille_2 = []
        self.nb_colonne = taille
        for i in range(int(int(self.nb_colonne))):
            for j in range(int(int(self.nb_colonne))):
                chiffre = str(chiffre_donné) + "  "
                grille_2.append(chiffre)
            self.grille.append(grille_2)
            grille_2 = []
        return self.grille

    def read_grid(self, path):
        with open(path, "w") as programme:
            programme.write('    ')
            for k in range(self.nb_colonne):
                programme.write(self.lst_lettre_min[k])
                programme.write('  ')
            programme.write('\n   ')
            programme.write(int(self.nb_colonne) * 3 * '-' + '-')
            programme.write('\n')
            for i in range(int(self.nb_colonne)):
                programme.write(self.lst_lettre_maj[i])
                programme.write(" | ")
                for j in range(len(self.grille[i])):
                    programme.write(str(self.grille[i][j]))
                programme.write("|")
                programme.write("\n")
            programme.write('   ')
            programme.write(int(self.nb_colonne) * 3 * '-' + '-')

    # Ces fonctions permettent d'afficher les variables dans d'autres class
    def return_grille(self):
        return self.grille

    def return_majuscule(self):
        return self.lst_lettre_maj

    def return_minuscule(self):
        return self.lst_lettre_min

    # Affichage des lettres
    def lettre_min(self):
        lim = 97 + int(int(self.nb_colonne))
        for i in range(97, lim):
            lettre_min = chr(i)
            lettre = lettre_min
            self.lst_lettre_min.append(lettre)

        return self.lst_lettre_min

    def lettre_maj(self):
        lim = 65 + int(int(self.nb_colonne))
        for i in range(65, lim):
            lettre_maj = chr(i)
            lettre = lettre_maj
            self.lst_lettre_maj.append(lettre)

        return self.lst_lettre_maj

    # FIn Affichage des Lettres

    # Figures
    def figure_triangle(self):
        min = int(self.nb_colonne) // 2
        max = (int(self.nb_colonne) // 2) + 1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = '.  '
            min -= 1
            max += 1

    def figure_losange(self):
        min = int(self.nb_colonne) // 2
        max = (int(self.nb_colonne) // 2) + 1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = '.  '
            min -= 1
            max += 1
        min = 0
        max = int(self.nb_colonne)
        for i in range(int(self.nb_colonne) // 2, int(self.nb_colonne) - 1):
            for j in range(min, max):
                self.grille[i][j] = '.  '
            min += 1
            max -= 1
        self.grille[int(self.nb_colonne) - 1][int(self.nb_colonne) // 2] = '.  '

    def figure_cercle(self, trou):
        # Haut Gauche
        max = int(self.nb_colonne) // 4
        min = 0
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            max -= 1
        # Haut Droit
        max = int(self.nb_colonne)
        min = int((3 / 4) * int(self.nb_colonne) + 1)
        for i in range(int(self.nb_colonne) // 4):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            min += 1
        # Bas Gauche
        max = int(self.nb_colonne) // 4
        min = 1
        for i in range(int((3 / 4) * int(self.nb_colonne) + 1), int(self.nb_colonne)):
            for j in range(min):
                self.grille[i][j] = str(trou) + '  '
            min += 1
        # Bas Droit
        max = int(self.nb_colonne)
        min = int(self.nb_colonne)
        for i in range(int((3 / 4) * int(self.nb_colonne) + 1), int(self.nb_colonne)):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            min -= 1
    # Fin Figures


class Forme:

    def __init__(self):
        self.lst_forme_reutilisable_tous = []

    def formes_tous(self):
        self.forme_tous_ensemble = []
        self.forme_tous_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_tous_2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_tous_3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_tous_4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0]]
        self.forme_tous_5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_tous_6 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
        self.forme_tous_7 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]
        self.forme_tous_8 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_tous_9 = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_tous_10 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_tous_11 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_tous_12 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_tous_13 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]]
        self.forme_tous_14 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_tous_15 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_tous_16 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_tous_17 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_tous_18 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_tous_19 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0]]
        self.forme_tous_20 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_tous_ensemble.append(self.forme_tous_1)
        self.forme_tous_ensemble.append(self.forme_tous_2)
        self.forme_tous_ensemble.append(self.forme_tous_3)
        self.forme_tous_ensemble.append(self.forme_tous_4)
        self.forme_tous_ensemble.append(self.forme_tous_5)
        self.forme_tous_ensemble.append(self.forme_tous_6)
        self.forme_tous_ensemble.append(self.forme_tous_7)
        self.forme_tous_ensemble.append(self.forme_tous_8)
        self.forme_tous_ensemble.append(self.forme_tous_9)
        self.forme_tous_ensemble.append(self.forme_tous_10)
        self.forme_tous_ensemble.append(self.forme_tous_11)
        self.forme_tous_ensemble.append(self.forme_tous_12)
        self.forme_tous_ensemble.append(self.forme_tous_13)
        self.forme_tous_ensemble.append(self.forme_tous_14)
        self.forme_tous_ensemble.append(self.forme_tous_15)
        self.forme_tous_ensemble.append(self.forme_tous_16)
        self.forme_tous_ensemble.append(self.forme_tous_17)
        self.forme_tous_ensemble.append(self.forme_tous_18)
        self.forme_tous_ensemble.append(self.forme_tous_19)
        self.forme_tous_ensemble.append(self.forme_tous_20)

        return self.forme_tous_ensemble

    def formes_triangle(self):
        self.forme_triangle_ensemble = []
        self.forme_triangle_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0]]
        self.forme_triangle_2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]]
        self.forme_triangle_3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_triangle_4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_triangle_5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_triangle_6 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.forme_triangle_7 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_triangle_8 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0]]
        self.forme_triangle_9 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_triangle_10 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_triangle_11 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_triangle_ensemble.append(self.forme_triangle_1)
        self.forme_triangle_ensemble.append(self.forme_triangle_2)
        self.forme_triangle_ensemble.append(self.forme_triangle_3)
        self.forme_triangle_ensemble.append(self.forme_triangle_4)
        self.forme_triangle_ensemble.append(self.forme_triangle_5)
        self.forme_triangle_ensemble.append(self.forme_triangle_6)
        self.forme_triangle_ensemble.append(self.forme_triangle_7)
        self.forme_triangle_ensemble.append(self.forme_triangle_8)
        self.forme_triangle_ensemble.append(self.forme_triangle_9)
        self.forme_triangle_ensemble.append(self.forme_triangle_10)
        self.forme_triangle_ensemble.append(self.forme_triangle_11)

        return self.forme_triangle_ensemble

    def formes_losange(self):
        self.forme_losange_ensemble = []
        self.forme_losange_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_losange_2 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]]
        self.forme_losange_3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
        self.forme_losange_4 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]
        self.forme_losange_5 = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]]
        self.forme_losange_6 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
        self.forme_losange_7 = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]]
        self.forme_losange_8 = [[0, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_losange_9 = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_losange_10 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
        self.forme_losange_11 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
        self.forme_losange_12 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
        self.forme_losange_13 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.forme_losange_14 = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_losange_ensemble.append(self.forme_losange_1)
        self.forme_losange_ensemble.append(self.forme_losange_2)
        self.forme_losange_ensemble.append(self.forme_losange_3)
        self.forme_losange_ensemble.append(self.forme_losange_4)
        self.forme_losange_ensemble.append(self.forme_losange_5)
        self.forme_losange_ensemble.append(self.forme_losange_6)
        self.forme_losange_ensemble.append(self.forme_losange_7)
        self.forme_losange_ensemble.append(self.forme_losange_8)
        self.forme_losange_ensemble.append(self.forme_losange_9)
        self.forme_losange_ensemble.append(self.forme_losange_10)
        self.forme_losange_ensemble.append(self.forme_losange_11)
        self.forme_losange_ensemble.append(self.forme_losange_12)
        self.forme_losange_ensemble.append(self.forme_losange_13)
        self.forme_losange_ensemble.append(self.forme_losange_14)

        return self.forme_losange_ensemble

    def formes_cercle(self):
        self.forme_cercle_ensemble = []
        self.forme_cercle_1 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
        self.forme_cercle_2 = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]]
        self.forme_cercle_3 = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]]
        self.forme_cercle_4 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]
        self.forme_cercle_5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0]]
        self.forme_cercle_6 = [[0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]]
        self.forme_cercle_7 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
        self.forme_cercle_8 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
        self.forme_cercle_9 = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.forme_cercle_10 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
        self.forme_cercle_11 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
        self.forme_cercle_12 = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 1, 1, 0]]
        self.forme_cercle_ensemble.append(self.forme_cercle_1)
        self.forme_cercle_ensemble.append(self.forme_cercle_2)
        self.forme_cercle_ensemble.append(self.forme_cercle_3)
        self.forme_cercle_ensemble.append(self.forme_cercle_4)
        self.forme_cercle_ensemble.append(self.forme_cercle_5)
        self.forme_cercle_ensemble.append(self.forme_cercle_6)
        self.forme_cercle_ensemble.append(self.forme_cercle_7)
        self.forme_cercle_ensemble.append(self.forme_cercle_8)
        self.forme_cercle_ensemble.append(self.forme_cercle_9)
        self.forme_cercle_ensemble.append(self.forme_cercle_10)
        self.forme_cercle_ensemble.append(self.forme_cercle_11)
        self.forme_cercle_ensemble.append(self.forme_cercle_12)

        return self.forme_cercle_ensemble

    def path_figure(self):
        self.path_figure = "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"

    def affichage_figure_write(self, figure):
        # "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"
        with open(self.path_figure, "w") as test_affichage_figure:
            for i in range(len(figure)):
                test_affichage_figure.write(str(i + 1))
                test_affichage_figure.write("\n")
                for j in range(len(figure[i])):
                    for k in range(len(figure[i][j])):
                        if figure[i][j][k] % 2 == 1:
                            test_affichage_figure.write("- ")
                        elif figure[i][j][k] % 2 == 0:
                            test_affichage_figure.write("0 ")
                    test_affichage_figure.write('\n')
                test_affichage_figure.write('\n')
        self.lst_forme_reutilisable_tous.append(figure)

    def affichage_figure_append(self, figure):
        # "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"
        with open(self.path_figure, "a") as test_affichage_figure:
            for i in range(len(figure)):
                test_affichage_figure.write(str(i + 1))
                test_affichage_figure.write("\n")
                for j in range(len(figure[i])):
                    for k in range(len(figure[i][j])):
                        if figure[i][j][k] % 2 == 1:
                            test_affichage_figure.write("- ")
                        elif figure[i][j][k] % 2 == 0:
                            test_affichage_figure.write("0 ")
                    test_affichage_figure.write('\n')
                test_affichage_figure.write('\n')
        self.lst_forme_reutilisable_tous.append(figure)

    def return_lst_forme_reutilisable(self):
        return self.lst_forme_reutilisable_tous


class Placement_figure:
    def __init__(self) -> None:
        Forme.__init__(self)
        Grille.__init__(self)
        self.placement_bloc_tous = False
        

    # Choix de la politique de suggestion
    def blocs_alea(self, figure_1, figure_2, nb_blocs_afficher):
        self.lst_alea = []
        self.lst_affichage_forme_alea = []
        self.lst_forme_reutilisable_alea = []

        for i in range(len(figure_1)):
            self.lst_alea.append(figure_1[i])
        for i in range(len(figure_2)):
            self.lst_alea.append(figure_2[i])

        

        print("\nVoici les choix que vous avez pour 'Affichage de 3 blocs aléatoire' : \n")

        for i in range(nb_blocs_afficher):
            # Création du nombre aléatoire
            nb_alea = rd.randint(0, len(self.lst_alea) - 1)

            self.lst_affichage_forme_alea.append(self.lst_alea[nb_alea])
            self.lst_forme_reutilisable_alea.append(self.lst_alea[nb_alea])
            # Suppression pour éviter la redondance
            del self.lst_alea[nb_alea]

            # Affichage de la forme
            for i in range(len(self.lst_affichage_forme_alea)):
                for j in range(len(self.lst_affichage_forme_alea[i])):
                    for k in range(len(self.lst_affichage_forme_alea[i][j])):
                        if self.lst_affichage_forme_alea[i][j][k] % 2 == 1:
                            print("-", end=" ")
                        elif self.lst_affichage_forme_alea[i][j][k] % 2 == 0:
                            print("0", end=" ")
                    print('\n')
            print('\n')
            del self.lst_affichage_forme_alea[i]
        print('\n')

        return self.lst_forme_reutilisable_alea

    def blocs_tous(self, figure_1, figure_2):
        Forme.path_figure(self)
        Forme.affichage_figure_write(self, figure_1)
        Forme.affichage_figure_append(self, figure_2)

    # FIN# Choix de la politique de suggestion

    # Placement du bloc
    def placement_bloc_alea(self, figure_1, figure_2, nb_blocs_afficher):

        self.placement_possible_alea = False
        self.placement_impossible_alea = False
        self.placement_final_alea = False

        while self.placement_final_alea == False:

            Placement_figure.blocs_alea(self, figure_1, figure_2, nb_blocs_afficher)

            print("\nChoississez un bloc")
            choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut : ")
            while choice_user_placement_bloc_alea < '1' or choice_user_placement_bloc_alea > '3':
                choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut : ")



            if choice_user_placement_bloc_alea == '1':
                self.forme_alea = self.lst_forme_reutilisable_alea[0]
            if choice_user_placement_bloc_alea == '2':
                self.forme_alea = self.lst_forme_reutilisable_alea[1]
            if choice_user_placement_bloc_alea == '3':
                self.forme_alea = self.lst_forme_reutilisable_alea[2]

            print("choisir les coordonnées pour poser votre bloc :")
            self.cordonnees_minuscule = str(input("Première coordonnée : "))
            while self.cordonnees_minuscule not in Grille.lettre_min(self):
                self.cordonnees_minuscule = str(input("Première coordonnée : "))
            self.cordonnees_majuscule = str(input("Seconde coordonnée : "))
            while self.cordonnees_majuscule not in Grille.lettre_maj(self):
                self.cordonnees_majuscule = str(input("Seconde coordonnée : "))

            Placement_figure.reduction_grille_xy(self,self.forme_alea)
            self.lst_inter_xy = self.lst_inter_x

            grille = Grille.return_grille(self)
            lst_min = Grille.return_minuscule(self)
            lst_maj = Grille.return_majuscule(self)
            index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
            index_lst_min = lst_min.index(self.cordonnees_minuscule)
            
            try:
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        #TEST -- print("\n",self.lst_inter_xy[i])

                        indent = i #+ len(self.lst_inter_xy)-1
                        extend = i

                        if self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == '.  ':
                            self.placement_possible_alea = True
                            #print("A")
                        elif self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == '2  ':
                            self.placement_impossible_alea = True
                            #print("B")
                        elif self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_impossible_alea = True
                            #print("C")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_possible_alea = True
                            #print("D")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == '.  ':
                            self.placement_possible_alea = True
                            #print("E")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == '2  ':
                            self.placement_possible_alea = True
                            #print("F")
                        #print(self.forme_alea[extend][j],grille[index_lst_maj + indent][index_lst_min + j])
                        #print(self.placement_possible_alea, self.placement_impossible_alea,"\n")
                
                 
                        
            except:
                print("Vous ne passerez pas")
                
            #TEST -- print("\n\n")

    
            if self.placement_impossible_alea == True or self.placement_possible_alea == False:
                print("Vous ne pouvez pas poser ce bloc ici lol")
                self.placement_final_alea = False
            elif self.placement_impossible_alea == False and self.placement_possible_alea == True:
                print("Vous pouvez placer ce bloc ici")
                self.placement_final_alea = True

            
            
            self.placement_impossible_alea = False
            

            

    def reduction_grille_xy(self,forme):
        self.lst_inter_x = []
        index_y = 5
        index_x = 0
        repeat_x = 1
        accept = False
        accept_none = False

        self.lst_inter_x = forme
    
        #Supprimer colonne
        for i in range(5):
            for j in range(index_y):

                if self.lst_inter_x[4][index_y-1] == 1: 
                    accept_none = True
                    break
                if self.lst_inter_x[3][index_y-1] == 1: 
                    accept_none = True
                    break
                if self.lst_inter_x[2][index_y-1] == 1: 
                    accept_none = True
                    break
                else: 
                    if self.lst_inter_x[i][index_y-1] == 1:
                        accept_none = True
                        break
                    elif self.lst_inter_x[i][index_y-1] == 0:
                        accept = True
                    else:
                        accept = False
                        accept_none = True
                
            #print("test :", accept, accept_none)
            
            if accept == True and accept_none == False:
                for i in range(len(self.lst_inter_x)):
                    del self.lst_inter_x[i][-1]
            
            index_y -= 1
            accept = False
        accept_none = False
        
        #Supprimer ligne
        for i in range(len(self.lst_inter_x)):
            if 1 in self.lst_inter_x[i]:
                repeat_x+=1
        
        #print(len(self.lst_inter_x), repeat_x)

        for i in range(len(self.lst_inter_x)-repeat_x):
            if 1 not in self.lst_inter_x[i]:
                del(self.lst_inter_x[index_x])
                index_x += 1
            
        #TEST --print(repeat_x != 1)
        if repeat_x != 1 and repeat_x <= 5:
            del(self.lst_inter_x[0])


        #TEST -- print("final : ", self.lst_inter_x)
        
        #TEST -- for i in range(len(self.lst_inter_x)):
            #TEST -- print(self.lst_inter_x[i])

        return self.lst_inter_x



    def placement_bloc_tous(self, figure_1, figure_2):

        self.placement_possible_tous = False
        self.placement_impossible_tous = False
        self.placement_final_tous = False
        self.erreur_tous = True

        Placement_figure.blocs_tous(self, figure_1, figure_2)
        print("\nLes figures possibles sont dans le fichier que vous avez spécifiez\n")

        while self.placement_final_tous == False:

            self.erreur_tous = True

            while self.erreur_tous == True:
                print("\nChoississez un bloc")
                choice_user_placement_bloc_tous = input("En partant du haut : ")

                if choice_user_placement_bloc_tous == '1':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][0]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '2':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][1]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '3':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][2]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '4':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][3]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '5':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][4]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '6':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][5]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '7':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][6]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '8':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][7]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '9':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][8]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '10':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][9]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '11':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][10]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '12':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][11]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '13':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][12]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '14':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][13]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '15':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][14]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '16':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][15]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '17':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][16]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '18':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][17]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '19':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][18]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '20':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][19]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '21':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][20]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '22':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][21]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '23':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][22]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '24':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][23]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '25':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][24]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '26':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][25]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '27':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][26]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '28':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][27]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '29':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][28]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '30':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][29]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '31':
                    self.forme = Forme.return_lst_forme_reutilisable(self)[0][30]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '32':
                    try:
                        self.forme = Forme.return_lst_forme_reutilisable(self)[0][31]
                        self.erreur_tous = False
                    except:
                        self.erreur_tous = True
                elif choice_user_placement_bloc_tous == '33':
                    try:
                        self.forme = Forme.return_lst_forme_reutilisable(self)[0][32]
                        self.erreur_tous = False
                    except:
                        self.erreur_tous = True
                elif choice_user_placement_bloc_tous == '34':
                    try:
                        self.forme = Forme.return_lst_forme_reutilisable(self)[0][33]
                        self.erreur_tous = False
                    except:
                        self.erreur_tous = True
                else:
                    self.erreur_tous = True

            print("choisir les coordonnées pour poser votre bloc :")
            self.cordonnees_minuscule = str(input("Première coordonnée : "))
            while self.cordonnees_minuscule not in Grille.lettre_min(self):
                self.cordonnees_minuscule = str(input("Première coordonnée : "))
            self.cordonnees_majuscule = str(input("Seconde coordonnée : "))
            while self.cordonnees_majuscule not in Grille.lettre_maj(self):
                self.cordonnees_majuscule = str(input("Seconde coordonnée : "))

            grille = Grille.return_grille(self)
            lst_min = Grille.return_minuscule(self)
            lst_maj = Grille.return_majuscule(self)
            index_lst_maj = lst_maj.index(self.cordonnees_majuscule) - 4
            index_lst_min = lst_min.index(self.cordonnees_minuscule)

            for i in range(self.lst_inter_xy):
                for j in range(self.lst_inter_xy):
                    if self.forme[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == '.  ':
                        self.placement_possible_tous = True
                    elif self.forme[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == '2  ':
                        self.placement_impossible_tous = True
                    elif self.forme_alea[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == '   ':
                        self.placement_impossible_tous = True
                    elif self.forme[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == '.  ':
                        self.placement_possible_tous = True
                    elif self.forme[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == '.  ':
                        self.placement_possible_tous = True

            if self.placement_impossible_tous == True or self.placement_possible_tous == False:
                print("Vous ne pouvez pas poser ce bloc ici")
                self.placement_final_tous = False
            elif self.placement_impossible_tous == False and self.placement_possible_tous == True:
                print("Vous pouvez placer ce bloc ici")
                self.placement_final_tous = True

            return self.placement_final_tous
    
    def placement_figures_grilles_alea(self):
        grille = Grille.return_grille(self)

        lst_min = Grille.return_minuscule(self)
        lst_maj = Grille.return_majuscule(self)
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
        index_lst_min = lst_min.index(self.cordonnees_minuscule)

        #for k in range(len(self.forme_alea)):
            #print(self.forme_alea[k])

        if self.placement_final_alea == True:
            #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))
            for i in range(len(self.lst_inter_xy)):
                for j in range(len(self.lst_inter_xy[i])):
                    
                    indent = i #+ len(self.lst_inter_xy)
                    extend = i

                    #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))

                    if Regle_du_jeu.return_choice_user_plateau(self) == '1' or Regle_du_jeu.return_choice_user_plateau(self) == '2':

                        if grille[index_lst_maj + indent][index_lst_min + j] == '2  '   and self.forme_alea[extend][j] == 1:
                            print("Vous ne pouvez pas poser ce bloc ici")

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '.  ' and self.forme_alea[extend][j] == 1:
                            forme_alea_str = '2'
                        
                        elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 1:
                            print("Impossible")

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '.  ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = '.'

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = ' '
        

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '2  ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = '2'

                        grille[index_lst_maj + i][index_lst_min + j] = forme_alea_str + '  '
                    
                    elif Regle_du_jeu.return_choice_user_plateau(self) == '3':

                        if grille[index_lst_maj + indent][index_lst_min + j] == '2  '   and self.forme_alea[extend][j] == 1:
                            print("Vous ne pouvez pas poser ce bloc ici")

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '.  ' and self.forme_alea[extend][j] == 1:
                            forme_alea_str = '2'
                        
                        elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 1:
                            print("Impossible")

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '.  ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = '.'

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = ' '
        

                        elif grille[index_lst_maj + indent][index_lst_min + j] == '2  ' and self.forme_alea[extend][j] == 0:
                            forme_alea_str = '2'

                        grille[index_lst_maj + i][index_lst_min + j] = forme_alea_str + '  '
                    

class Point:
    def __init__(self):
        Grille.__init__(self)
        Forme.__init__(self)
        Placement_figure.__init__(self)
        self.grille_point = Grille.return_grille(self)
        self.choice_user = Regle_du_jeu.return_choice_user_plateau
        self.point_final = 0
        self.point = 0
        


    ### Points des lignes
    
    def points_ligne(self):
        grille_2 = []
        grille_2.append(Grille.return_grille(self))
        arret = False

        for i in range(len(self.grille_point)):
            #print(self.grille_point[t])
            if ('.  ' not in self.grille_point[i] or '.  ' not in self.grille_point[0]) or '.  ' not in self.grille_point[-1]:

                while True:
                    for j in range(len(self.grille_point)):
                        if '.  ' not in self.grille_point[i]:
                            if self.grille_point[i][j] == '2  ':
                                self.grille_point[i][j] = '.  '
                                self.point += 1
                        

                    while arret == False:
                        for k in range(-2, -len(self.grille_point)-1, -1):
                            for l in range(len(self.grille_point)):

                                '''if self.grille_point[-1][l] == '2  ':
                                    self.grille_point[-1][l] == '.  '''''
                                
                                if self.grille_point[0][l] == '2  ':
                                    self.grille_point[0][l] == '.  '
                                
                                if self.grille_point[k+1][l] == '   ':
                                    self.grille_point[k][l] == self.grille_point[k][l]

                                elif self.grille_point[k][l] == '2  ':
                                    self.grille_point[k+1][l] = self.grille_point[k][l]
                                    self.grille_point[k][l] = '.  '
                        arret = True
                    break

                
                       
    ### Points des colonnes

    def points_colonne(self):
        grille_2 = []
        
        for i in range(len(self.grille_point)):
            for j in range(len(self.grille_point)):
                grille_2.append(self.grille_point[j][i])
                #TEST -- print(grille_2,"\n")
            for k in range(len(self.grille_point)):
                if '.  ' not in grille_2:
                    #TEST -- print("\ngood\n")
                    if self.grille_point[k][i] == '2  ':
                        self.grille_point[k][i] = '.  '
                        self.point += 1
            grille_2 = []


    ### MAIN 

    def return_point(self):
        return self.point
 


class Regle_du_jeu:
    def __init__(self):
        Grille.__init__(self)
        Forme.__init__(self)
        Placement_figure.__init__(self)
        Point.__init__(self)
        self.nb_colonne = 0
        

    def affichage(self, choice= None):
        emoji_fete = "\U0001F389"
        emoji_valentin = "\U0001F468"
        emoji_joss = "\U0001F996"



        print(8*'-')
        print("\n\n",emoji_fete, "TETRIS, Opus II", emoji_fete,"\n\n")
        print("Vous êtes sur l'écran d'acceuil, on vous laisse découvrir : \n")
        print("1 - Commmencer à jouer")
        print("2 - Afficher les règles du jeu")
        print("3 - Copyright")
        print("\n")

        #Choix chemin accès
        print("Choississez le chemin d'accès vers votre figure : ")
        #self.path = input("")
        self.path = "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt"

        self.choice_user = input("Faire votre choix (1, 2, 3) : ")
        while self.choice_user < '1' or self.choice_user > '3':
            self.choice_user = input("Faire votre choix (1, 2, 3) : ")


        if self.choice_user == '1' or choice == 1:

            self.nb_colonne = input("\nDonner le taille de votre tableau (21, 23 ou 25) : ")
            while (self.nb_colonne != '21' and self.nb_colonne != '23') and self.nb_colonne != '25':
                self.nb_colonne = input("Donner le taille de votre tableau (21, 23 ou 25) : ")

            print("\nChoississez votre plateau de jeu :")
            print("1 - Triangle")
            print("2 - Losange")
            print("3 - Cercle")
            self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")
            while self.choice_user_plateau < '1' or self.choice_user_plateau > '3':
                self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")

            Grille.lettre_min(self)
            Grille.lettre_maj(self)

            if self.choice_user_plateau == '1':  # Triangle
                Grille.create_grid(self, ' ', int(self.nb_colonne))
                Grille.figure_triangle(self)
                self.politique_suggestion_blocs()
                Grille.read_grid(self, self.path)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_triangle(self))
                    Placement_figure.placement_figures_grilles_alea(self)
                    Forme.formes_tous(self)
                    Forme.formes_triangle(self)

                    Grille.read_grid(self, self.path)
                    tm.sleep(.5)

                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()

                    Grille.read_grid(self, self.path)
                    Forme.formes_tous(self)
                    Forme.formes_triangle(self)
                
                    
                    
                

            if self.choice_user_plateau == '2':  # Losange
                Grille.create_grid(self, ' ', int(self.nb_colonne))
                Grille.figure_losange(self)
                self.politique_suggestion_blocs()
                Grille.read_grid(self, self.path)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_losange(self))
                    Placement_figure.placement_figures_grilles_alea(self)                    
                    Forme.formes_tous(self)
                    Forme.formes_losange(self)

                    Grille.read_grid(self, self.path)
                    tm.sleep(.5)
                    
                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()
                    
                    Grille.read_grid(self, self.path)
                    Forme.formes_tous(self)
                    Forme.formes_losange(self)
                    
                
                    
                    

            if self.choice_user_plateau == '3':  # Cercle
                Grille.create_grid(self, '.', int(self.nb_colonne))
                Grille.figure_cercle(self,' ')
                self.politique_suggestion_blocs()
                Grille.read_grid(self, self.path)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_cercle(self))
                    Placement_figure.placement_figures_grilles_alea(self)
                    Forme.formes_tous(self)
                    Forme.formes_cercle(self)

                    Grille.read_grid(self, self.path)
                    tm.sleep(.5)


                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()
                    
                    Grille.read_grid(self, self.path)
                    Forme.formes_tous(self)
                    Forme.formes_cercle(self)
                
                    
                   
                   
        if self.choice_user == '2':
            # Mettre les règle ici
            print("Le joueur peut choisir une surface selon les trois formes possibles: Cercle, losange ou triangle. Il disposera d'un ensemble de blocs qu'il devra placer tour à tour sur la surface valide du plateau en saisissant les coordonnées de l’endroit où il veut les insérer.")
            Regle_du_jeu.affichage(self)

        
        if self.choice_user == '3':
            print("\n")
            lst_author = ["Valentin Menon","Joss Douniama Okana"]
            print("{} {:^25} {}".format(emoji_valentin, lst_author[0], emoji_valentin))
            print("{} {:^25} {}".format(emoji_joss, lst_author[1], emoji_joss))
            print("\n")
            print("Pour retourner au menu, taper 1")
            self.choice_user_copyright = input("Faites votre choix : ")
            while self.choice_user_copyright != '1':
                self.choice_user_copyright = input("Faites votre choix : ")
            
            if self.choice_user_copyright == '1':
                self.affichage()
            
            



    def politique_suggestion_blocs(self):
        print("\nVous avez le choix entre deux suggestion de blocs :")
        print("1 - Affichage de l'ensemble des blocs du jeu")
        print("2 - Affichage de 3 blocs aléatoires")
        self.choice_user_politique_suggestion = input("Faite votre choix : ")
        while self.choice_user_politique_suggestion < '1' or self.choice_user_politique_suggestion > '2':
            self.choice_user_politique_suggestion = input("Faite votre choix : ")
        
    def politique_suggestion_blocs_2(self, figure_1_suggestion, figure_2_suggestion):
        if self.choice_user_politique_suggestion == '1':
            Placement_figure.placement_bloc_tous(self, figure_1_suggestion, figure_2_suggestion)
        if self.choice_user_politique_suggestion == '2':
            Placement_figure.placement_bloc_alea(self, figure_1_suggestion, figure_2_suggestion, 3)
        
    def return_choice_user_plateau(self):
        return self.choice_user_plateau
    
    def affichage_points(self):
        print("good")
        print("Vous avez {} points".format(Point.return_point(self)))



if __name__ == "__main__":
    Regle_du_jeu().affichage()
    
