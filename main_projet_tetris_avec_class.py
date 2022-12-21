import random as rd
import time as tm
import sys

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

    def read_grid(self, path, vertical_para, horizontal_para, coin_bg, coin_hg, coin_bd, coin_hd):

        
        horizontal = (self.nb_colonne * 4) * horizontal_para + horizontal_para
        vertical = vertical_para + " "

        with open(path, "w", encoding="utf-8") as programme:

            programme.write('      ')
            for k in range(self.nb_colonne):
                programme.write(self.lst_lettre_min[k])
                programme.write("   ")
            programme.write('\n   ')

            programme.write(coin_hg)
            programme.write(horizontal)
            programme.write(coin_hd)

            programme.write('\n')
            for i in range(int(self.nb_colonne)):
                programme.write(self.lst_lettre_maj[i])
                programme.write("  ")
                programme.write(vertical)
                for j in range(len(self.grille[i])):
                    programme.write(" ")
                    programme.write(str(self.grille[i][j]))
                programme.write(vertical_para)
                programme.write("\n")
            programme.write('   ')
            programme.write(coin_bg)
            programme.write(horizontal)
            programme.write(coin_bd)

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
    def figure_triangle(self, carre_vide):
        min = int(self.nb_colonne) // 2
        max = (int(self.nb_colonne) // 2) + 1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = carre_vide + "  "
            min -= 1
            max += 1

    def figure_losange(self, carre_vide):
        min = int(self.nb_colonne) // 2
        max = (int(self.nb_colonne) // 2) + 1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = carre_vide + "  "
            min -= 1
            max += 1
        min = 0
        max = int(self.nb_colonne)
        for i in range(int(self.nb_colonne) // 2, int(self.nb_colonne) - 1):
            for j in range(min, max):
                self.grille[i][j] = carre_vide + "  "
            min += 1
            max -= 1
        self.grille[int(self.nb_colonne) - 1][int(self.nb_colonne) // 2] = carre_vide + "  "

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

    
    def affichage_figure_write(self, figure, path, carre_vide, carre_plein):

        vide = carre_vide + " "
        plein = carre_plein + " "
        
        with open(path, "w", encoding="utf-8") as test_affichage_figure:
            for i in range(len(figure)):
                test_affichage_figure.write(str(i + 1))
                test_affichage_figure.write("\n")
                for j in range(len(figure[i])):
                    for k in range(len(figure[i][j])):
                        if figure[i][j][k] % 2 == 1:
                            test_affichage_figure.write(plein)
                        elif figure[i][j][k] % 2 == 0:
                            test_affichage_figure.write(vide)
                    test_affichage_figure.write('\n')
                test_affichage_figure.write('\n')
        self.lst_forme_reutilisable_tous.append(figure)

    def affichage_figure_append(self, figure, path, carre_vide, carre_plein):

        vide = carre_vide + " "
        plein = carre_plein + " "
        
        with open(path, "a", encoding="utf-8") as test_affichage_figure:
            for i in range(len(figure)):
                test_affichage_figure.write(str(i + 21))
                test_affichage_figure.write("\n")
                for j in range(len(figure[i])):
                    for k in range(len(figure[i][j])):
                        if figure[i][j][k] % 2 == 1:
                            test_affichage_figure.write(plein)
                        elif figure[i][j][k] % 2 == 0:
                            test_affichage_figure.write(vide)
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
    def blocs_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein):
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
                            print(plein, end=" ")
                        elif self.lst_affichage_forme_alea[i][j][k] % 2 == 0:
                            print(vide, end=" ")
                    print('')
            print('\n')
            del self.lst_affichage_forme_alea[i]
        print('\n')

        return self.lst_forme_reutilisable_alea

    def blocs_tous(self, figure_1, figure_2, path_figure, vide, plein):
        
        Forme.affichage_figure_write(self, figure_1, path_figure, vide, plein)
        Forme.affichage_figure_append(self, figure_2, path_figure, vide, plein)

    # FIN # Choix de la politique de suggestion

    # Placement du bloc
    def placement_bloc_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein):

        self.placement_possible_alea = False
        self.placement_impossible_alea = False
        self.placement_final_alea = False

        while self.placement_final_alea == False:

            Placement_figure.blocs_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein)

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
            self.cordonnees_minuscule = str(input("Première coordonnée ( minuscule ): "))
            while self.cordonnees_minuscule not in Grille.lettre_min(self):
                self.cordonnees_minuscule = str(input("Première coordonnée ( minuscule ): "))
            self.cordonnees_majuscule = str(input("Seconde coordonnée ( majuscule ): "))
            while self.cordonnees_majuscule not in Grille.lettre_maj(self):
                self.cordonnees_majuscule = str(input("Seconde coordonnée ( majuscule ): "))

            Placement_figure.reduction_grille_xy(self,self.forme_alea)
            self.lst_inter_xy = self.lst_inter_x

            grille = Grille.return_grille(self)
            lst_min = Grille.return_minuscule(self)
            lst_maj = Grille.return_majuscule(self)
            index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
            index_lst_min = lst_min.index(self.cordonnees_minuscule)

            vide_long = vide + "  "
            plein_long = plein + "  "
            
            try:
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        #TEST -- print("\n",self.lst_inter_xy[i])

                        indent = i #+ len(self.lst_inter_xy)-1
                        extend = i

                        if self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == vide_long:
                            self.placement_possible_alea = True
                            #print("A")
                        elif self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == plein_long:
                            self.placement_impossible_alea = True
                            #print("B")
                        elif self.forme_alea[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_impossible_alea = True
                            #print("C")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_possible_alea = True
                            #print("D")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == vide_long:
                            self.placement_possible_alea = True
                            #print("E")
                        elif self.forme_alea[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == plein_long:
                            self.placement_possible_alea = True
                            #print("F")
                        #print(self.forme_alea[extend][j],grille[index_lst_maj + indent][index_lst_min + j])
                        #print(self.placement_possible_alea, self.placement_impossible_alea,"\n")
                
                 
                        
            except:
                print("Vous ne passerez pas")
                
            #TEST -- print("\n\n")

    
            if self.placement_impossible_alea == True or self.placement_possible_alea == False:
                print("Vous ne pouvez pas poser ce bloc ici")
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



    def placement_bloc_tous(self, figure_1, figure_2, path_figure, vide, plein):

        self.placement_possible_tous = False
        self.placement_impossible_tous = False
        self.placement_final_tous = False
        self.erreur_tous = True

        

        Placement_figure.blocs_tous(self, figure_1, figure_2, path_figure, vide, plein)
        #print(len(Forme.return_lst_forme_reutilisable(self)[0]))
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
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][1]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '3':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][2]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '4':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][3]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '5':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][4]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '6':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][5]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '7':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][6]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '8':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][7]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '9':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][8]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '10':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][9]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '11':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][10]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '12':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][11]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '13':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][12]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '14':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][13]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '15':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][14]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '16':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][15]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '17':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][16]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '18':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][17]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '19':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][18]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '20':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[0][19]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '21':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][0]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '22':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][1]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '23':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][2]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '24':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][3]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '25':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][4]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '26':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][5]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '27':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][6]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '28':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][7]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '29':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][8]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '30':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][9]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '31':
                    self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][10]
                    self.erreur_tous = False
                elif choice_user_placement_bloc_tous == '32':
                    try:
                        self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][11]
                        self.erreur_tous = False
                    except:
                        self.erreur_tous = True
                elif choice_user_placement_bloc_tous == '33':
                    try:
                        self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][12]
                        self.erreur_tous = False
                    except:
                        self.erreur_tous = True
                elif choice_user_placement_bloc_tous == '34':
                    try:
                        self.forme_tous = Forme.return_lst_forme_reutilisable(self)[1][13]
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

            Placement_figure.reduction_grille_xy(self,self.forme_tous)
            self.lst_inter_xy = self.lst_inter_x

            grille = Grille.return_grille(self)
            lst_min = Grille.return_minuscule(self)
            lst_maj = Grille.return_majuscule(self)
            index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
            index_lst_min = lst_min.index(self.cordonnees_minuscule)

            vide_long = vide + "  "
            plein_long = plein + "  "

            try:
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        #TEST -- print("\n",self.lst_inter_xy[i])

                        indent = i #+ len(self.lst_inter_xy)-1
                        extend = i

                        if self.forme_tous[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == vide_long:
                            self.placement_possible_tous = True
                            #print("A")
                        elif self.forme_tous[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == plein_long:
                            self.placement_impossible_tous = True
                            #print("B")
                        elif self.forme_tous[extend][j] == 1 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_impossible_tous = True
                            #print("C")
                        elif self.forme_tous[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == '   ':
                            self.placement_possible_tous = True
                            #print("D")
                        elif self.forme_tous[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == vide_long:
                            self.placement_possible_tous = True
                            #print("E")
                        elif self.forme_tous[extend][j] == 0 and grille[index_lst_maj + indent][index_lst_min + j] == plein_long:
                            self.placement_possible_tous = True
                            #print("F")
                        #print(self.forme_alea[extend][j],grille[index_lst_maj + indent][index_lst_min + j])
                        #print(self.placement_possible_alea, self.placement_impossible_alea,"\n")
                
                 
                        
            except:
                print("Vous ne passerez pas")

            if self.placement_impossible_tous == True or self.placement_possible_tous == False:
                print("Vous ne pouvez pas poser ce bloc ici")
                self.placement_final_tous = False
            elif self.placement_impossible_tous == False and self.placement_possible_tous == True:
                print("Vous pouvez placer ce bloc ici")
                self.placement_final_tous = True

            return self.placement_final_tous
    
    def placement_figures_grilles_alea(self, vide, plein):
        grille = Grille.return_grille(self)

        lst_min = Grille.return_minuscule(self)
        lst_maj = Grille.return_majuscule(self)
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
        index_lst_min = lst_min.index(self.cordonnees_minuscule)

        vide_long = vide + "  "
        plein_long = plein + "  "



        #for k in range(len(self.forme_alea)):
            #print(self.forme_alea[k])

        try :
            if self.placement_final_alea == True:
                #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        
                        indent = i #+ len(self.lst_inter_xy)
                        extend = i

                        #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))

                        if Regle_du_jeu.return_choice_user_plateau(self) == '1' or Regle_du_jeu.return_choice_user_plateau(self) == '2':

                            if grille[index_lst_maj + indent][index_lst_min + j] == plein_long   and self.forme_alea[extend][j] == 1:
                                print("Vous ne pouvez pas poser ce bloc ici")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_alea[extend][j] == 1:
                                forme_alea_str = plein
                            
                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 1:
                                print("Impossible")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_alea[extend][j] == 0:
                                forme_alea_str = vide

                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 0:
                                forme_alea_str = ' '
            

                            elif grille[index_lst_maj + indent][index_lst_min + j] == plein_long and self.forme_alea[extend][j] == 0:
                                forme_alea_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_alea_str + '  '
                        
                        elif Regle_du_jeu.return_choice_user_plateau(self) == '3':

                            if grille[index_lst_maj + indent][index_lst_min + j] == plein_long   and self.forme_alea[extend][j] == 1:
                                print("Vous ne pouvez pas poser ce bloc ici")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_alea[extend][j] == 1:
                                forme_alea_str = plein
                            
                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 1:
                                print("Impossible")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_alea[extend][j] == 0:
                                forme_alea_str = vide

                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_alea[extend][j] == 0:
                                forme_alea_str = ' '
            

                            elif grille[index_lst_maj + indent][index_lst_min + j] == plein_long and self.forme_alea[extend][j] == 0:
                                forme_alea_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_alea_str + '  '
        
        except: 
            if self.placement_final_tous == True:
                #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        
                        indent = i #+ len(self.lst_inter_xy)
                        extend = i

                        #TEST -- print(Regle_du_jeu.return_choice_user_plateau(self))

                        if Regle_du_jeu.return_choice_user_plateau(self) == '1' or Regle_du_jeu.return_choice_user_plateau(self) == '2':

                            if grille[index_lst_maj + indent][index_lst_min + j] == plein_long   and self.forme_tous[extend][j] == 1:
                                print("Vous ne pouvez pas poser ce bloc ici")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_tous[extend][j] == 1:
                                forme_tous_str = plein
                            
                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_tous[extend][j] == 1:
                                print("Impossible")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_tous[extend][j] == 0:
                                forme_tous_str = vide

                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_tous[extend][j] == 0:
                                forme_tous_str = ' '
            

                            elif grille[index_lst_maj + indent][index_lst_min + j] == plein_long and self.forme_tous[extend][j] == 0:
                                forme_tous_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_tous_str + '  '
                        
                        elif Regle_du_jeu.return_choice_user_plateau(self) == '3':

                            if grille[index_lst_maj + indent][index_lst_min + j] == plein_long   and self.forme_tous[extend][j] == 1:
                                print("Vous ne pouvez pas poser ce bloc ici")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_tous[extend][j] == 1:
                                forme_tous_str = plein
                            
                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_tous[extend][j] == 1:
                                print("Impossible")

                            elif grille[index_lst_maj + indent][index_lst_min + j] == vide_long and self.forme_tous[extend][j] == 0:
                                forme_tous_str = vide

                            elif grille[index_lst_maj + indent][index_lst_min + j] == '   ' and self.forme_tous[extend][j] == 0:
                                forme_tous_str = ' '
            

                            elif grille[index_lst_maj + indent][index_lst_min + j] == plein_long and self.forme_tous[extend][j] == 0:
                                forme_tous_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_tous_str + '  '
                        

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
        emoji_valentin = "\U0001f4bb"
        emoji_joss = "\U0001F996"
        emoji_jeu = "\U0001F3AE"
        emoji_rule = "\U0001f4d6"
        emoji_copyright = "\U0001FAAA"
        emoji_cercle = "\u23FA\uFE0F"
        emoji_triangle = "\U0001f53c"
        emoji_losange = "\u23F9\uFE0F"
        emoji_aleatoire = "\U0001f3b2"
        emoji_tous = "\u267E\uFE0F"
        emoji_check = "	\u2714\uFE0F"
        emoji_mode_de_jeu = "\U0001f39f\uFE0F"

        emoji_carre_plein = "\u25A0"
        emoji_carre_vide = "\u25A1"

        emoji_ligne_vertical = '\U00002551'
        emoji_ligne_horizontal = '\U00002550'

        emoji_coin_hg = "\u2554"
        emoji_coin_hd = "\u2557"
        emoji_coin_bg = "\u255A"
        emoji_coin_bd = "\u255D"

        



        print("\n\n{:^75}".format(20*emoji_ligne_horizontal))
        print("\n\n{:^75}\n\n".format(emoji_fete + "  TETRIS, Opus II (v1.0)  " + emoji_fete))
        print("{:^75}\n\n".format(20*emoji_ligne_horizontal))

        #Choix chemin accès
        print("Avant toute chose, initialisons votre jeu : \n\n")
        print("Choississez le chemin d'accès vers votre plateau (sous la forme : 'C:\\...\\...\\...') : ")
        self.path = input("")
        #self.path = "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt"
        print("Choississez un chemin d'accès pour le fichier contenant toutes vos figures (sous la forme : 'C:\\...\\...\\...') : ")
        self.path_figure = input("")
        self.path_figure = "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"


        print("Vous êtes sur l'écran d'accueil, on vous laisse découvrir : \n")
        print("1 - {} Commmencer à jouer".format(emoji_jeu))
        print("2 - {} Afficher les règles du jeu".format(emoji_rule))
        print("3 - {}  Copyright".format(emoji_copyright))
        print("\n")

        

        self.choice_user = input("Faire votre choix (1, 2, 3) : ")
        while self.choice_user < '1' or self.choice_user > '3':
            self.choice_user = input("Faire votre choix (1, 2, 3) : ")


        if self.choice_user == '1' or choice == 1:

            self.nb_colonne = input("\nChoississez à présent la taille de votre tableau (21, 23 ou 25) : ")
            while (self.nb_colonne != '21' and self.nb_colonne != '23') and self.nb_colonne != '25':
                self.nb_colonne = input("Choississez à présent la taille de votre tableau (21, 23 ou 25) : ")

            print("\nChoississez votre plateau de jeu :")
            print("1 - {} Triangle".format(emoji_triangle))
            print("2 - {}  Losange".format(emoji_losange))
            print("3 - {}  Cercle".format(emoji_cercle))
            self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")
            while self.choice_user_plateau < '1' or self.choice_user_plateau > '3':
                self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")

            Grille.lettre_min(self)
            Grille.lettre_maj(self)

            if self.choice_user_plateau == '1':  # Triangle
                Grille.create_grid(self, ' ', int(self.nb_colonne))
                Grille.figure_triangle(self, emoji_carre_vide)
                self.politique_suggestion_blocs(emoji_aleatoire, emoji_tous)
                Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_triangle(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Placement_figure.placement_figures_grilles_alea(self, emoji_carre_vide, emoji_carre_plein)
                    Forme.formes_tous(self)
                    Forme.formes_triangle(self)

                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    tm.sleep(.5)

                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()

                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Forme.formes_tous(self)
                    Forme.formes_triangle(self)
                
                    
                    
                

            if self.choice_user_plateau == '2':  # Losange
                Grille.create_grid(self, ' ', int(self.nb_colonne))
                Grille.figure_losange(self, emoji_carre_vide)
                self.politique_suggestion_blocs(emoji_aleatoire, emoji_tous)
                Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_losange(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Placement_figure.placement_figures_grilles_alea(self, emoji_carre_vide, emoji_carre_plein)                   
                    Forme.formes_tous(self)
                    Forme.formes_losange(self)
                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()

                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    tm.sleep(.5)
                    
                    
                    
                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Forme.formes_tous(self)
                    Forme.formes_losange(self)
                    
                
                    
                    

            if self.choice_user_plateau == '3':  # Cercle
                Grille.create_grid(self, emoji_carre_vide, int(self.nb_colonne))
                Grille.figure_cercle(self, ' ')
                self.politique_suggestion_blocs(emoji_aleatoire, emoji_tous)
                Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    self.politique_suggestion_blocs_2(Forme.formes_tous(self), Forme.formes_cercle(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Placement_figure.placement_figures_grilles_alea(self, emoji_carre_vide, emoji_carre_plein)
                    Forme.formes_tous(self)
                    Forme.formes_cercle(self)

                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    tm.sleep(.5)


                    Point.points_ligne(self)
                    Point.points_colonne(self)
                    self.affichage_points()
                    
                    Grille.read_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Forme.formes_tous(self)
                    Forme.formes_cercle(self)
                
                    
                   
                   
        if self.choice_user == '2':
            print("\n\n\n")
            print("{:^75}\n\n".format("Règles du jeu"))
            print(emoji_check, " - Objectif : Gagner le plus de points")
            print(emoji_check, " - Déroulement : Choississez un plateau de jeu ( triangle, cercle ou losange ) et choississez parmi les deux modes de jeu : ")
            print(emoji_mode_de_jeu, "Mode de jeu : aléatoire ==> 3 blocs aléatoire vous sont proposer")
            print(emoji_mode_de_jeu, "Mode de jeu :    tous   ==> Vous avez le choix de tous les blocs affiliés au plateau")

            print(emoji_check, " - Placer le bloc à partir de ses coordonnées en bas à gauche")


            self.affichage()

        
        if self.choice_user == '3':
            print("\n\n\n")
            print("{:^75}\n\n".format("Collaborateurs")) 
            lst_author = ["Valentin Menon","Joss Douniama Okana"]
            print("{} {:^25} {}".format(emoji_valentin, lst_author[0], emoji_valentin))
            print("{} {:^25} {}".format(emoji_joss, lst_author[1], emoji_joss))
            
            self.affichage()
            
            



    def politique_suggestion_blocs(self, emoji_alea, emoji_tous):
        print("\nVous avez le choix entre deux suggestion de blocs :")
        print("1 - {}  Affichage de l'ensemble des blocs du jeu".format(emoji_tous))
        print("2 - {} Affichage de 3 blocs aléatoires".format(emoji_alea))
        self.choice_user_politique_suggestion = input("Faite votre choix (1, 2): ")
        while self.choice_user_politique_suggestion < '1' or self.choice_user_politique_suggestion > '2':
            self.choice_user_politique_suggestion = input("Faite votre choix (1, 2): ")
        
    def politique_suggestion_blocs_2(self, figure_1_suggestion, figure_2_suggestion, path_figure, vide, plein):
        if self.choice_user_politique_suggestion == '1':
            Placement_figure.placement_bloc_tous(self, figure_1_suggestion, figure_2_suggestion, path_figure, vide, plein)
        if self.choice_user_politique_suggestion == '2':
            Placement_figure.placement_bloc_alea(self, figure_1_suggestion, figure_2_suggestion, 3, vide, plein)
        
    def return_choice_user_plateau(self):
        return self.choice_user_plateau
    
    def affichage_points(self):
        emoji_ligne_horizontal = '\U00002550'

        print("\n", 10*emoji_ligne_horizontal)
        print("Vous avez {} points".format(Point.return_point(self)))
        print("",10*emoji_ligne_horizontal, "\n")



if __name__ == "__main__":
    Regle_du_jeu().affichage()
    
