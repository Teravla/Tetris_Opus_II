




############################################################
### Program Tetris Opus II                               ###
###                                                      ###
### Author : Valentin Menon, Joss Douniama Okana         ###
###                                                      ###
### Version : v1.0.5, 22/12/2022                         ###
############################################################


#Library Import
import random as rd
import time as tm
import sys

#Variables globales

version_of_game = "v 1.0.5"


#Any function related to the grid
class Grid:

    def __init__(self):
        ### Initialization function
        self.grille = []
        self.lst_letter_maj = []
        self.lst_letter_min = [] 


    #Creation and reading of the grid
    def create_grid(self, chiffre_donne, taille):
        ### Creation of the grid
        ##### chiffre_donne : Background
        ##### taille        : tray size
        grille_2 = []
        self.nb_colonne = taille
        for i in range(int(int(self.nb_colonne))):
            for j in range(int(int(self.nb_colonne))):
                chiffre = str(chiffre_donne) + "  "
                grille_2.append(chiffre)
            self.grille.append(grille_2)
            grille_2 = []
        return self.grille

    def reading_grid(self, path, vertical_para, horizontal_para, coin_bg, coin_hg, coin_bd, coin_hd):
        ### Display the grid in a .txt
        ##### path : path to the .txt file
        ##### vertical_para   : vertical border 
        ##### horizontal_para : horizontal border
        ##### coin_xx         : corner of the tray

        
        horizontal = (self.nb_colonne * 4) * horizontal_para + horizontal_para
        vertical = vertical_para + " "

        with open(path, "w", encoding="utf-8") as programme:

            programme.write('      ')
            for k in range(self.nb_colonne):
                programme.write(Grid.letter_lower(self)[k])
                programme.write("   ")
            programme.write('\n   ')

            programme.write(coin_hg)
            programme.write(horizontal)
            programme.write(coin_hd)

            programme.write('\n')
            for i in range(int(self.nb_colonne)):
                programme.write(Grid.letter_capital(self)[i])
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
    ####


    #Return Function for other class
    def return_grid(self):
        return self.grille

    def return_capital(self):
        return self.lst_letter_maj

    def return_lower(self):
        return self.lst_letter_min
    ####


    #Display of letters
    def letter_lower(self):
        ### Create a list with all lower letter
        lim = 97 + int(int(self.nb_colonne))
        for i in range(97, lim):
            letter_min = chr(i)
            lettre = letter_min
            self.lst_letter_min.append(lettre)

        return self.lst_letter_min
    

    def letter_capital(self):
        ### Create a list with all capital letter
        lim = 65 + int(int(self.nb_colonne))
        for i in range(65, lim):
            letter_maj = chr(i)
            lettre = letter_maj
            self.lst_letter_maj.append(lettre)

        return self.lst_letter_maj
    ####


    #Shapes
    def shape_triangle(self, carre_vide):
        ### Create a triangle tray 
        ##### carre_vide : shape of the empty slot in the tray
        min = int(self.nb_colonne) // 2
        max = (int(self.nb_colonne) // 2) + 1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = carre_vide + "  "
            min -= 1
            max += 1

    def shape_diamond(self, carre_vide):
        ### Create a diamond tray 
        ##### carre_vide : shape of the empty slot in the tray
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

    def shape_circular(self, trou):
        ### Create a circular tray, This function works differently, it filled the grid with empty slots and created the holes to form a circle
        ##### trou : background, empty slots

        # Top Left
        max = int(self.nb_colonne) // 4
        min = 0
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            max -= 1
        # Top Right
        max = int(self.nb_colonne)
        min = int((3 / 4) * int(self.nb_colonne) + 1)
        for i in range(int(self.nb_colonne) // 4):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            min += 1
        # Bottom Left
        max = int(self.nb_colonne) // 4
        min = 1
        for i in range(int((3 / 4) * int(self.nb_colonne) + 1), int(self.nb_colonne)):
            for j in range(min):
                self.grille[i][j] = str(trou) + '  '
            min += 1
        # Bottom Right
        max = int(self.nb_colonne)
        min = int(self.nb_colonne)
        for i in range(int((3 / 4) * int(self.nb_colonne) + 1), int(self.nb_colonne)):
            for j in range(min, max):
                self.grille[i][j] = str(trou) + '  '
            min -= 1
    ####



#Any function related to shapes
class Shape:

    def __init__(self):
        ### Initialization function
        self.lst_forme_reutilisable_tous = []

    #Shapes common to all trays
    def shape_all(self):
        ### Shapes common to all trays
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

    #Shapes common to the tray ==> Triangle
    def shape_triangle(self):
        ### Shapes common to the tray ==> Triangle
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


    #Shapes common to the tray ==> Diamond
    def shape_diamond(self):
        ### Shapes common to the tray ==> Diamond
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


    #Shapes common to the tray ==> Circle
    def shape_circular(self):
        ### Shapes common to the tray ==> Circle
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

    
    #Writing shapes in a .txt for user policy: all blocks
    def display_figure_write(self, figure, path, carre_vide, carre_plein):
        ### The shapes come from two different functions (all shapes + tray-specific shapes). This function writes in the .txt one of the first shape group
        ##### figure      : One of the first shape group
        ##### path        : path to the .txt file
        ##### carre_vide  : empty slot
        ##### carre_plein : full slot


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

        

    def display_figure_append(self, figure, path, carre_vide, carre_plein):
        ### The shapes come from two different functions (all shapes + tray-specific shapes). This function writes in the .txt the other shape group
        ##### figure      : One of the first shape group
        ##### path        : path to the .txt file
        ##### carre_vide  : empty slot
        ##### carre_plein : full slot

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
    ####
    
        
    #Return Function for other class
    def return_lst_reuse_shape(self):
        return self.lst_forme_reutilisable_tous
    ####



#Any function related to bloc placing
class Figure_placement:

    def __init__(self) -> None:
        ### Initialization function
        Shape.__init__(self)
        Grid.__init__(self)
        
        self.erreur_placement = 0
        
        self.placement_bloc_all = False
        

    #Choice of blocks in the case of user policy ==> random blocks
    def blocs_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein, diff, language):
        ### Initializes the creation and display of random blocks
        ##### figure_1          : one of the shape group
        ##### figure_2          : the other shape group
        ##### nb_blocs_afficher : number of random blocks displayed
        ##### vide              : empty slot
        ##### plein             : full slot
        ##### diff              : difficulty (number of chance)

        self.lst_alea = []
        self.lst_affichage_forme_alea = []
        self.lst_forme_reutilisable_alea = []

        for i in range(len(figure_1)):
            self.lst_alea.append(figure_1[i])
        for i in range(len(figure_2)):
            self.lst_alea.append(figure_2[i])

        #display of points
        Point.points_line(self, vide, plein)
        Point.points_column(self, vide, plein)
        Rule_of_the_game.point_display(self, language)
        Rule_of_the_game.remaining_chance(self, diff, language)
        ##

        
        if language == "fr":
            print("\nVoici les choix que vous avez pour '{} -- Affichage de {} blocs aléatoire -- {}' : \n".format(vide, diff, plein))
        elif language == "en":
            print("\nHere are the choices you have for '{} -- Display of {} random blocks -- {}' : \n".format(vide, diff, plein))
        

        for i in range(nb_blocs_afficher):

            #Creation of the random number
            nb_alea = rd.randint(0, len(self.lst_alea) - 1)
            ##

            self.lst_affichage_forme_alea.append(self.lst_alea[nb_alea])
            self.lst_forme_reutilisable_alea.append(self.lst_alea[nb_alea])

            #Delete to avoid redundancy
            del self.lst_alea[nb_alea]
            ##

            

            #Shape display
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
            ##

        print('\n')

        return self.lst_forme_reutilisable_alea
    ####


    #Placement of blocks in case of user policy ==> random blocks
    def placement_bloc_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein, target, min, maj, bad, good, diff, language):
        ### Checks if the shape can be posed
        ##### figure_1           : one of the shape group
        ##### figure_2           : the other shape group
        ##### nb_blocs_afficher  : number of random blocks displayed
        ##### vide               : empty slot
        ##### plein              : full slot
        ##### target, min, maj, bad, good : emoji
        ##### diff               : difficulty


        self.placement_possible_alea = False
        self.placement_impossible_alea = False
        self.placement_final_alea = False
        grille = Grid.return_grid(self)
        lst_min = Grid.return_lower(self)
        lst_maj = Grid.return_capital(self)
        vide_long = vide + "  "
        plein_long = plein + "  "
        error = "\u274C"


        Figure_placement.blocs_alea(self, figure_1, figure_2, nb_blocs_afficher, vide, plein, diff, language)

        

        #Block Selection
        if language == "fr":
            print("\nChoississez un bloc")
            choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut (4 pour Menu) : ")
            while choice_user_placement_bloc_alea < '1' or choice_user_placement_bloc_alea > '4':
                choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut (4 pour Menu): ")
        elif language == "en":
            print("\nChoose a block")
            choice_user_placement_bloc_alea = input("1, 2 or 3 from the top (4 for Menu) : ")
            while choice_user_placement_bloc_alea < '1' or choice_user_placement_bloc_alea > '4':
                choice_user_placement_bloc_alea = input("1, 2 or 3 from the top (4 for Menu): ")

        if choice_user_placement_bloc_alea == '1':
            self.forme_alea = self.lst_forme_reutilisable_alea[0]
        if choice_user_placement_bloc_alea == '2':
            self.forme_alea = self.lst_forme_reutilisable_alea[1]
        if choice_user_placement_bloc_alea == '3':
            self.forme_alea = self.lst_forme_reutilisable_alea[2]
        if choice_user_placement_bloc_alea == '4':
            Rule_of_the_game.display(self)
        #--# Add conditions as part of displaying more blocks (default : 3)
        ##

        #Block coordinates
        print("\n")
        if language == "fr":
            print(target, "- Choisir les coordonnées pour poser votre bloc :")
            print(min, "-- Première coordonnée ( minuscule ): ", end="")
            self.cordonnees_minuscule = str(input(""))
            while self.cordonnees_minuscule not in Grid.letter_lower(self):
                print(min, "-- Première coordonnée ( minuscule ): ", end="")
                self.cordonnees_minuscule = str(input(""))

            print(maj, "-- Seconde coordonnée ( majuscule ): ", end="")
            self.cordonnees_majuscule = str(input(""))
            while self.cordonnees_majuscule not in Grid.letter_capital(self):
                print(maj, "-- Seconde coordonnée ( majuscule ): ", end="")
                self.cordonnees_majuscule = str(input(""))
        elif language == "en":
            print(target, "- Choose the coordinates to place your block :")
            print(min, "-- First coordinate ( lower case ): ", end="")
            self.cordonnees_minuscule = str(input(""))
            while self.cordonnees_minuscule not in Grid.letter_lower(self):
                print(min, "-- First coordinate ( lower case ): ", end="")
                self.cordonnees_minuscule = str(input(""))

            print(maj, "-- Second coordinate ( upper case ): ", end="")
            self.cordonnees_majuscule = str(input("")) 
            while self.cordonnees_majuscule not in Grid.letter_capital(self):
                print(maj, "-- Second coordinate ( upper case ): ", end="")
        ##

        #Variable requiring the user’s prior choice
        Figure_placement.reduction_grid_xy(self,self.forme_alea)
        self.lst_inter_xy = self.lst_inter_x
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
        index_lst_min = lst_min.index(self.cordonnees_minuscule)
        ##
        
        #Check the possibility of placing a block
        try:
            for i in range(len(self.lst_inter_xy)):
                for j in range(len(self.lst_inter_xy[i])):

                    if self.forme_alea[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == vide_long:
                        self.placement_possible_alea = True
                    elif self.forme_alea[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == plein_long:
                        self.placement_impossible_alea = True
                    elif self.forme_alea[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == '   ':
                        self.placement_impossible_alea = True
                    elif self.forme_alea[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == '   ':
                        self.placement_possible_alea = True
                    elif self.forme_alea[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == vide_long:
                        self.placement_possible_alea = True
                    elif self.forme_alea[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == plein_long:
                        self.placement_possible_alea = True
        except:
            print(error, " -- Error -- ", error)
            print("Contact the admin")
        ##

        #Final Check
        if language == "fr":
            if self.placement_impossible_alea == True or self.placement_possible_alea == False:
                print("\n")
                print("{} {:^5} {}".format(bad, " Vous ne pouvez pas poser ce  bloc ici", bad))
                self.placement_final_alea = False
                self.erreur_placement += 1
            elif self.placement_impossible_alea == False and self.placement_possible_alea == True:
                print("\n")
                print("{} {:^5} {}".format(good, " Vous pouvez poser ce  bloc ici", good))
                self.placement_final_alea = True
        elif language == "en":
            if self.placement_impossible_alea == True or self.placement_possible_alea == False:
                print("\n")
                print("{} {:^5} {}".format(bad, " You can't put this block here", bad))
                self.placement_final_alea = False
                self.erreur_placement += 1
            elif self.placement_impossible_alea == False and self.placement_possible_alea == True:
                print("\n")
                print("{} {:^5} {}".format(good, " You can put this block here", good))
                self.placement_final_alea = True
        ##

        self.placement_impossible_alea = False
    ####


    #This function reduces the shape of the block to a minimum so that it can be placed on the edge of the tray and avoid errors: out of range. 
    def reduction_grid_xy(self,forme):
        ### Reduces the figure to the maximum in order to be able to place it along the trays
        ##### Forme : shape

        self.lst_inter_x = []
        index_y = 5
        index_x = 0
        repeat_x = 1
        accept = False
        accept_none = False
        self.lst_inter_x = forme
    
        #Delete the column
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
            
            if accept == True and accept_none == False:
                for i in range(len(self.lst_inter_x)):
                    del self.lst_inter_x[i][-1]
            
            index_y -= 1
            accept = False
        accept_none = False
        ##
        
        #Delete the line 
        for i in range(len(self.lst_inter_x)):
            if 1 in self.lst_inter_x[i]:
                repeat_x+=1

        for i in range(len(self.lst_inter_x)-repeat_x):
            if 1 not in self.lst_inter_x[i]:
                del(self.lst_inter_x[index_x])
                index_x += 1

        if repeat_x != 1 and repeat_x <= 5:
            del(self.lst_inter_x[0])
        ##

        #Returns the reduced form
        return self.lst_inter_x
    ####


    #Choice of blocks in the case of user policy ==> all blocks
    def blocs_all(self, figure_1, figure_2, path_figure, vide, plein, diff, language):
        ### Initializes the creation and display of all blocks
        ##### figure_1    : one of the shape group
        ##### figure_2    : the other shape group
        ##### path_figure : path to the .txt where all the blocks are
        ##### vide        : empty slot
        ##### plein       : full slot
        ##### diff        : difficulty (number of chance)
        
        Shape.display_figure_write(self, figure_1, path_figure, vide, plein)
        Shape.display_figure_append(self, figure_2, path_figure, vide, plein)

        #display of points
        Point.points_line(self, vide, plein)
        Point.points_column(self, vide, plein)
        Rule_of_the_game.point_display(self, language)
        Rule_of_the_game.remaining_chance(self, diff, language)
        ##
    ####


    #Placement of blocks in case of user policy ==> all blocks
    def placement_bloc_all(self, figure_1, figure_2, path_figure, vide, plein, target, min, maj, bad, good, diff, language):
        ### Checks if the shape can be posed
        ##### figure_1    : one of the shape group
        ##### figure_2    : the other shape group
        ##### path_figure : path to the .txt where all the blocks are
        ##### vide        : empty slot
        ##### plein       : full slot
        ##### target, min, maj, bad, good : emoji
        ##### diff        : difficulty

        Figure_placement.blocs_all(self, figure_1, figure_2, path_figure, vide, plein, diff, language)

        self.placement_possible_tous = False
        self.placement_impossible_tous = False
        self.placement_final_tous = False
        self.erreur_tous = True
        self.erreur_placement = 0
        grille = Grid.return_grid(self)
        lst_min = Grid.return_lower(self)
        lst_maj = Grid.return_capital(self)
        vide_long = vide + "  "
        plein_long = plein + "  "
        error = "\u274C"

        if language == "fr":
            print("\nLes figures possibles sont dans le fichier que vous avez spécifié\n")
        elif language == "en":
            print("\nThe possible figures are in the file you specified\n")

        #User Choice
        
        self.erreur_tous = True
        while self.erreur_tous == True:
            if language == "fr":
                print("\nChoississez un bloc")
                choice_user_placement_bloc_all = input("En partant du haut (35 pour Menu): ")
                while choice_user_placement_bloc_all < '1' or choice_user_placement_bloc_all > '35':
                    choice_user_placement_bloc_all = input("En partant du haut (35 pour Menu): ")
            elif language == "en": 
                print("\nChoose a block")
                choice_user_placement_bloc_all = input("Starting from the top (35 for Menu): ")
                while choice_user_placement_bloc_all < '1' or choice_user_placement_bloc_all > '35':
                    choice_user_placement_bloc_all = input("Starting from the top (35 for Menu): ")

            if choice_user_placement_bloc_all == '1':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][0]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '2':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][1]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '3':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][2]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '4':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][3]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '5':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][4]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '6':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][5]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '7':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][6]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '8':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][7]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '9':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][8]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '10':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][9]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '11':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][10]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '12':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][11]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '13':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][12]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '14':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][13]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '15':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][14]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '16':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][15]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '17':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][16]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '18':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][17]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '19':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][18]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '20':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[0][19]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '21':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][0]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '22':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][1]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '23':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][2]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '24':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][3]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '25':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][4]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '26':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][5]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '27':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][6]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '28':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][7]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '29':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][8]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '30':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][9]
                self.erreur_tous = False
            elif choice_user_placement_bloc_all == '31':
                self.forme_tous = Shape.return_lst_reuse_shape(self)[1][10]
                self.erreur_tous = False

            #This is because some trays have more shapes than others
            elif choice_user_placement_bloc_all == '32':
                try:
                    self.forme_tous = Shape.return_lst_reuse_shape(self)[1][11]
                    self.erreur_tous = False
                except:
                    self.erreur_tous = True
            elif choice_user_placement_bloc_all == '33':
                try:
                    self.forme_tous = Shape.return_lst_reuse_shape(self)[1][12]
                    self.erreur_tous = False
                except:
                    self.erreur_tous = True
            elif choice_user_placement_bloc_all == '34':
                try:
                    self.forme_tous = Shape.return_lst_reuse_shape(self)[1][13]
                    self.erreur_tous = False
                except:
                    self.erreur_tous = True
            else:
                self.erreur_tous = True

            if choice_user_placement_bloc_all == '35':
                Rule_of_the_game.display(self)
    ##


        #Block coordinates
        print("\n")
        if language == "fr":
            print(target, "- Choisir les coordonnées pour poser votre bloc :")
            print(min, "-- Première coordonnée ( minuscule ): ", end="")
            self.cordonnees_minuscule = str(input(""))
            while self.cordonnees_minuscule not in Grid.letter_lower(self):
                print(min, "-- Première coordonnée ( minuscule ): ", end="")
                self.cordonnees_minuscule = str(input(""))

            print(maj, "-- Seconde coordonnée ( majuscule ): ", end="")
            self.cordonnees_majuscule = str(input(""))
            while self.cordonnees_majuscule not in Grid.letter_capital(self):
                print(maj, "-- Seconde coordonnée ( majuscule ): ", end="")
                self.cordonnees_majuscule = str(input(""))
        elif language == "en":
            print(target, "- Choose the coordinates to place your block :")
            print(min, "-- First coordinate ( lower case ): ", end="")
            self.cordonnees_minuscule = str(input(""))
            while self.cordonnees_minuscule not in Grid.letter_lower(self):
                print(min, "-- First coordinate ( lower case ): ", end="")
                self.cordonnees_minuscule = str(input(""))

            print(maj, "-- Second coordinate ( upper case ): ", end="")
            self.cordonnees_majuscule = str(input("")) 
            while self.cordonnees_majuscule not in Grid.letter_capital(self):
                print(maj, "-- Second coordinate ( upper case ): ", end="")
        ##

        #Variable requiring the user’s prior choice
        Figure_placement.reduction_grid_xy(self,self.forme_tous)
        self.lst_inter_xy = self.lst_inter_x
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
        index_lst_min = lst_min.index(self.cordonnees_minuscule)
        ##

        
        #Check the possibility of placing a block
        try:
            for i in range(len(self.lst_inter_xy)):
                for j in range(len(self.lst_inter_xy[i])):
                
                    if self.forme_tous[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == vide_long:
                        self.placement_possible_tous = True
                    elif self.forme_tous[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == plein_long:
                        self.placement_impossible_tous = True
                    elif self.forme_tous[i][j] == 1 and grille[index_lst_maj + i][index_lst_min + j] == '   ':
                        self.placement_impossible_tous = True
                    elif self.forme_tous[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == '   ':
                        self.placement_possible_tous = True
                    elif self.forme_tous[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == vide_long:
                        self.placement_possible_tous = True
                    elif self.forme_tous[i][j] == 0 and grille[index_lst_maj + i][index_lst_min + j] == plein_long:
                        self.placement_possible_tous = True
        except:
            print(error, " -- Error -- ", error)
            print("Contact the admin")
        ##

        #Final Check
        if language == "fr":
            if self.placement_impossible_tous == True or self.placement_possible_tous == False:
                print("\n")
                print("{} {:^5} {}".format(bad, " Vous ne pouvez pas poser ce  bloc ici", bad))
                self.placement_final_tous = False
                self.erreur_placement += 1
            elif self.placement_impossible_tous == False and self.placement_possible_tous == True:
                print("\n")
                print("{} {:^5} {}".format(good, " Vous pouvez poser ce  bloc ici", good))
                self.placement_final_tous = True
        elif language == "en":
            if self.placement_impossible_tous == True or self.placement_possible_tous == False:
                print("\n")
                print("{} {:^5} {}".format(bad, " You can't put this block here", bad))
                self.placement_final_tous = False
                self.erreur_placement += 1
            elif self.placement_impossible_tous == False and self.placement_possible_tous == True:
                print("\n")
                print("{} {:^5} {}".format(good, " You can put this block here", good))
                self.placement_final_tous = True
        ##

        return self.placement_final_tous
    ####


    #Function of placing blocks on the tray in the .txt
    def placement_shape_grid(self, vide, plein):
        ### Place the shape on the tray
        ##### vide : empty slot
        ##### plein : full slot

        grille = Grid.return_grid(self)

        lst_min = Grid.return_lower(self)
        lst_maj = Grid.return_capital(self)
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-len(self.lst_inter_xy)+1
        index_lst_min = lst_min.index(self.cordonnees_minuscule)
        vide_long = vide + "  "
        plein_long = plein + "  "

        #Display of blocks in case of user policy ==> random blocks
        try :
            if self.placement_final_alea == True:
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):
                        
                        if (Rule_of_the_game.return_choice_user_tray(self) == '1' or Rule_of_the_game.return_choice_user_tray(self) == '2') or Rule_of_the_game.return_choice_user_tray(self) == '3':

                            if grille[index_lst_maj + i][index_lst_min + j] == plein_long   and self.forme_alea[i][j] == 1:
                                print("Contact Admin, error 0X00")

                            elif grille[index_lst_maj + i][index_lst_min + j] == vide_long and self.forme_alea[i][j] == 1:
                                forme_alea_str = plein
                            
                            elif grille[index_lst_maj + i][index_lst_min + j] == '   ' and self.forme_alea[i][j] == 1:
                                print("Contact Admin, error 0x01")

                            elif grille[index_lst_maj + i][index_lst_min + j] == vide_long and self.forme_alea[i][j] == 0:
                                forme_alea_str = vide

                            elif grille[index_lst_maj + i][index_lst_min + j] == '   ' and self.forme_alea[i][j] == 0:
                                forme_alea_str = ' '
            

                            elif grille[index_lst_maj + i][index_lst_min + j] == plein_long and self.forme_alea[i][j] == 0:
                                forme_alea_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_alea_str + '  '
        ##

        #Display of blocks in case of user policy ==> all blocks               
        except: 
            if self.placement_final_tous == True:
                for i in range(len(self.lst_inter_xy)):
                    for j in range(len(self.lst_inter_xy[i])):

                        if (Rule_of_the_game.return_choice_user_tray(self) == '1' or Rule_of_the_game.return_choice_user_tray(self) == '2') or Rule_of_the_game.return_choice_user_tray(self) == '3':

                            if grille[index_lst_maj + i][index_lst_min + j] == plein_long   and self.forme_tous[i][j] == 1:
                                print("Contact Admin, error 0X10")

                            elif grille[index_lst_maj + i][index_lst_min + j] == vide_long and self.forme_tous[i][j] == 1:
                                forme_tous_str = plein
                            
                            elif grille[index_lst_maj + i][index_lst_min + j] == '   ' and self.forme_tous[i][j] == 1:
                                print("Contact Admin, error 0X11")

                            elif grille[index_lst_maj + i][index_lst_min + j] == vide_long and self.forme_tous[i][j] == 0:
                                forme_tous_str = vide

                            elif grille[index_lst_maj + i][index_lst_min + j] == '   ' and self.forme_tous[i][j] == 0:
                                forme_tous_str = ' '
            

                            elif grille[index_lst_maj + i][index_lst_min + j] == plein_long and self.forme_tous[i][j] == 0:
                                forme_tous_str = plein

                            grille[index_lst_maj + i][index_lst_min + j] = forme_tous_str + '  '
        ##
    ####

    #Return Function for other class
    def return_error_point(self):
        return self.erreur_placement
       
    ####


                        
#Any function related to point management
class Point:

    def __init__(self):
        ### Initialization function
        Grid.__init__(self)
        Shape.__init__(self)
        Figure_placement.__init__(self)
        self.grille_point = Grid.return_grid(self)
        self.choice_user = Rule_of_the_game.return_choice_user_tray
        self.point_final = 0
        self.point = 0
        

    #Line points
    def points_line(self, vide, plein):
        ### Checks lines and removes them if they are full and adding points to user
        ##### vide : empty slot
        ##### plein : full slot

        grille_2 = []
        grille_2.append(Grid.return_grid(self))
        arret = False
        plein_long = plein + "  "
        vide_long = vide + "  "

        for i in range(len(self.grille_point)):
            if (vide_long not in self.grille_point[i] or vide_long not in self.grille_point[0]) or vide_long not in self.grille_point[-1]:

                while True:
                    for j in range(len(self.grille_point)):
                        if vide_long not in self.grille_point[i]:
                            if self.grille_point[i][j] == plein_long:
                                self.grille_point[i][j] = vide_long
                                self.point += 1

                    while arret == False:
                        for k in range(-2, -len(self.grille_point)-1, -1):
                            for l in range(len(self.grille_point)):
                                
                                
                                if self.grille_point[0][l] == plein_long:
                                    self.grille_point[0][l] == vide_long
                                
                                if self.grille_point[k+1][l] == '   ':
                                    self.grille_point[k][l] == self.grille_point[k][l]

                                elif self.grille_point[k][l] == plein_long:
                                    self.grille_point[k+1][l] = self.grille_point[k][l]
                                    self.grille_point[k][l] = vide_long
                        arret = True
                    break
    ####


    #Column points
    def points_column(self, vide, plein):
        ### Checks columns and removes them if they are full adding points to user
        ##### vide : empty slot
        ##### plein : full slot

        grille_2 = []
        plein_long = plein + "  "
        vide_long = vide + "  "
        
        for i in range(len(self.grille_point)):
            for j in range(len(self.grille_point)):
                grille_2.append(self.grille_point[j][i])
            for k in range(len(self.grille_point)):
                if vide_long not in grille_2:
                    if self.grille_point[k][i] == plein_long:
                        self.grille_point[k][i] = vide_long
                        self.point += 1
            grille_2 = []
    ####

    # Return Function for other class 
    def return_point(self):
        return self.point
    ####
 


#Main Fonctions
class Rule_of_the_game:

    def __init__(self):
        ### Initialization function
        Grid.__init__(self)
        Shape.__init__(self)
        Figure_placement.__init__(self)
        Point.__init__(self)
        self.nb_colonne = 0
        

    def display(self, difficulte=3, mode_diff="Moyen", language="fr", nb_colonne=21):
        ### Main Function, display the menu to user
        ##### difficulte : Difficulty 
        ##### mode_diff  : Display the difficulty

        #Emoji 
        emoji_fete = "\U0001F389"
        emoji_valentin = "\U0001f4bb"
        emoji_joss = "\U0001F996"
        emoji_jeu = "\U0001F3AE"
        emoji_jeu_2 = "\t\U0001f579\uFE0F"
        emoji_rule = "\U0001f4d6"
        emoji_copyright = "\U0001FAAA"
        emoji_cercle = "\u23FA\uFE0F"
        emoji_triangle = "\U0001f53c"
        emoji_losange = "\u23F9\uFE0F"
        emoji_aleatoire = "\U0001f3b2"
        emoji_tous = "\u267E\uFE0F"
        emoji_check = "\u2714\uFE0F"
        emoji_mode_de_jeu = "\t\U0001f39f\uFE0F"
        emoji_target = "\U0001f3af"
        emoji_min = "\U0001f521"
        emoji_maj ="\U0001f520"
        emoji_good = "\u2705"
        emoji_bad = "\u274E"
        emoji_setting = "\u2699\uFE0F"
        emoji_diff = "\U0001f39a\uFE0F"
        emoji_diff_1 = "\u2795"
        emoji_diff_2 = "\U0001f53c"
        emoji_diff_3 = "\u23EB"
        emoji_diff_4 = "\U0001f64f"
        emoji_flag = "\U0001f38c"
        emoji_fr = "\U0001f1eb\U0001f1f7"
        emoji_en = "\U0001f1ec\U0001f1e7"

        emoji_carre_plein = "\u25A0"
        emoji_carre_vide = "\u25A1"

        emoji_ligne_vertical = '\U00002551'
        emoji_ligne_horizontal = '\U00002550'
        emoji_coin_hg = "\u2554"
        emoji_coin_hd = "\u2557"
        emoji_coin_bg = "\u255A"
        emoji_coin_bd = "\u255D"
        ##


        #Function call
        Grid.letter_lower(self)
        Grid.letter_capital(self)


        #Title display
        print("\n\n{:^75}".format(20*emoji_ligne_horizontal))
        print("\n\n{:^75}\n\n".format(emoji_fete + "  TETRIS, Opus II ({})  ".format(version_of_game) + emoji_fete))
        print("{:^75}\n\n".format(20*emoji_ligne_horizontal))
        ##


        #Choosing the path to .txt
        
        '''if language == "fr":
            print("Avant toute chose, initialisons votre jeu : \n\n")
            print("Choississez le chemin d'accès vers votre plateau (sous la forme : C:\...\...\...) : ")
            self.path = input("")
            print("Choississez un chemin d'accès pour le fichier contenant toutes vos figures (sous la forme : C:\...\...\...) : ")
            self.path_figure = input("")

        elif language == 'en':
            print("First of all, let's initialize your game : \n\n")
            print("Choose the path to your tray (in the form: C:\...\...\...) : ")
            self.path = input("")
            print("Choose a path for the file containing all your figures (in the form: C:\...\...\...) : ")
            self.path_figure = input("")'''
        

        self.path = ".\\programme.txt"
        self.path_figure = ".\\test_figure.txt"
        ##


        #Home screen
        if language == "fr":
            
            print("Vous êtes sur l'écran d'accueil, on vous laisse découvrir : \n")
            print("1 - {} Commmencer à jouer".format(emoji_jeu))
            print("2 - {} Afficher les règles du jeu".format(emoji_rule))
            print("3 - {}  Copyright".format(emoji_copyright))
            print("4 - {}  Paramètres".format(emoji_diff))
            print("\n")
            
            self.choice_user = input("Faire votre choix (1, 2, 3, 4) : ")
            while self.choice_user < '1' or self.choice_user > '4':
                self.choice_user = input("Faire votre choix (1, 2, 3, 4) : ")

        elif language == "en":
            print("You are on the home screen, we let you discover :  : \n")
            print("1 - {} Start playing".format(emoji_jeu))
            print("2 - {} Display the rules of the game".format(emoji_rule))
            print("3 - {}  Copyright".format(emoji_copyright))
            print("4 - {}  Settings".format(emoji_diff))
            print("\n")
            
            self.choice_user = input("Make your choice (1, 2, 3, 4) : ")
            while self.choice_user < '1' or self.choice_user > '4':
                self.choice_user = input("Make your choice (1, 2, 3, 4) : ")

        ##

        


        if self.choice_user == '1':

            #Choice of tray size
            if language == "fr":
                self.nb_colonne = input("\nChoississez à présent la taille de votre tableau (21, 23 ou 25)  (26 pour Menu) : ")
                while (self.nb_colonne != '21' and self.nb_colonne != '23') and self.nb_colonne != '26':
                    self.nb_colonne = input("Choississez à présent la taille de votre tableau (21, 23 ou 25) (26 pour Menu) : ")
            
            elif language == "en":
                self.nb_colonne = input("\nNow choose the size of your table (21, 23 or 25) (26 for Menu) : ")
                while (self.nb_colonne != '21' and self.nb_colonne != '23') and self.nb_colonne != '26':
                    self.nb_colonne = input("Now choose the size of your table (21, 23 or 25) (26 for Menu) : ")

            if self.nb_colonne == '26':
                Rule_of_the_game.display(self)
            ##


            #Tray selection

            if language == "fr":
                print("\nChoisissez votre plateau de jeu :")
                print("1 - {} Triangle".format(emoji_triangle))
                print("2 - {}  Losange".format(emoji_losange))
                print("3 - {}  Cercle".format(emoji_cercle))
                print("4 - {} Menu".format(emoji_bad))
                self.choice_user_plateau = input("Faire votre choix (1, 2, 3, 4) : ")
                while self.choice_user_plateau < '1' or self.choice_user_plateau > '4':
                    self.choice_user_plateau = input("Faire votre choix (1, 2, 3, 4) : ")
            
            elif language == "en":
                print("\nChoose your game board :")
                print("1 - {} Triangle".format(emoji_triangle))
                print("2 - {}  Diamond".format(emoji_losange))
                print("3 - {}  Circle".format(emoji_cercle))
                print("4 - {} Menu".format(emoji_bad))
                self.choice_user_plateau = input("Make your choice (1, 2, 3, 4) : ")
                while self.choice_user_plateau < '1' or self.choice_user_plateau > '4':
                    self.choice_user_plateau = input("Make your choice (1, 2, 3, 4) : ")
            
            if self.choice_user_plateau == '4':
                Rule_of_the_game.display(self)
            


            if self.choice_user_plateau == '1':  # Triangle
                Grid.create_grid(self, ' ', int(self.nb_colonne))
                Grid.shape_triangle(self, emoji_carre_vide)
                self.user_policy(emoji_aleatoire, emoji_tous, language)
                Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    Shape.shape_all(self)
                    Shape.shape_triangle(self)
                    Shape.__init__(self)
                    Shape.display_figure_write(self, Shape.shape_all(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Shape.display_figure_append(self, Shape.shape_triangle(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    self.user_policy_2(Shape.shape_all(self), Shape.shape_triangle(self), self.path_figure, emoji_carre_vide, emoji_carre_plein, emoji_target, emoji_min, emoji_maj, emoji_bad, emoji_good, difficulte, language)
                    Figure_placement.placement_shape_grid(self, emoji_carre_vide, emoji_carre_plein)
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Point.points_line(self, emoji_carre_vide, emoji_carre_plein)
                    Point.points_column(self, emoji_carre_vide, emoji_carre_plein)
                    tm.sleep(.5)
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    
                    
            if self.choice_user_plateau == '2':  # Diamond
                Grid.create_grid(self, ' ', int(self.nb_colonne))
                Grid.shape_diamond(self, emoji_carre_vide)
                self.user_policy(emoji_aleatoire, emoji_tous, language)
                Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    Shape.shape_all(self)
                    Shape.shape_diamond(self)
                    Shape.__init__(self)
                    Shape.display_figure_write(self, Shape.shape_all(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Shape.display_figure_append(self, Shape.shape_diamond(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    self.user_policy_2(Shape.shape_all(self), Shape.shape_diamond(self), self.path_figure, emoji_carre_vide, emoji_carre_plein, emoji_target, emoji_min, emoji_maj, emoji_bad, emoji_good, difficulte, language)
                    Figure_placement.placement_shape_grid(self, emoji_carre_vide, emoji_carre_plein)             
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Point.points_line(self, emoji_carre_vide, emoji_carre_plein)
                    Point.points_column(self, emoji_carre_vide, emoji_carre_plein)
                    tm.sleep(.5)
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    
                    
                
            if self.choice_user_plateau == '3':  # Circle
                Grid.create_grid(self, emoji_carre_vide, int(self.nb_colonne))
                Grid.shape_circular(self, ' ')
                self.user_policy(emoji_aleatoire, emoji_tous, language)
                Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                while True:
                    Shape.shape_all(self)
                    Shape.shape_circular(self)
                    Shape.__init__(self)
                    Shape.display_figure_write(self, Shape.shape_all(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    Shape.display_figure_append(self, Shape.shape_circular(self), self.path_figure, emoji_carre_vide, emoji_carre_plein)
                    self.user_policy_2(Shape.shape_all(self), Shape.shape_circular(self), self.path_figure, emoji_carre_vide, emoji_carre_plein, emoji_target, emoji_min, emoji_maj, emoji_bad, emoji_good, difficulte, language)
                    Figure_placement.placement_shape_grid(self, emoji_carre_vide, emoji_carre_plein)
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    Point.points_line(self, emoji_carre_vide, emoji_carre_plein)
                    Point.points_column(self, emoji_carre_vide, emoji_carre_plein)
                    tm.sleep(.5)
                    Grid.reading_grid(self, self.path, emoji_ligne_vertical, emoji_ligne_horizontal, emoji_coin_bg, emoji_coin_hg, emoji_coin_bd, emoji_coin_hd)
                    
            
            else:
                Rule_of_the_game.display(self)
            ##
                
        #Help Menu
        if self.choice_user == '2':
            print("\n\n\n")

            if language == "fr":
                print("{:^75}\n\n".format("Règles du jeu"))
                print(emoji_check, " - Objectif : Gagner le plus de points")
                print(emoji_check, " - Déroulement : Choississez un plateau de jeu ( triangle, cercle ou losange ) et choississez parmi les deux modes de jeu : ")
                print(emoji_mode_de_jeu, "Mode de jeu : aléatoire ==> 1, 2 ou 3 blocs aléatoire vous sont proposer")
                print(emoji_mode_de_jeu, "Mode de jeu :    tous   ==> Vous avez le choix de tous les blocs affiliés au plateau")
                print(emoji_check, " - Placer le bloc à partir de ses coordonnées en bas à gauche")
                print(emoji_check, " - Vous avez {} chances (mode {})".format(difficulte, mode_diff))
                print(emoji_check, " - Pour les difficultés, si vous choississez les blocs aléatoires, le nombre de bloc diffère : ")
                print(emoji_jeu_2, "| {:^5} | : 3 blocs".format("Facile"))
                print(emoji_jeu_2, "| {:^5}  | : 3 blocs".format("Moyen"))
                print(emoji_jeu_2, "| {:^5}  | : 2 blocs".format("Dur"))
                print(emoji_jeu_2, "| {:^5}  | : 1 bloc".format("God"))

            elif language == "en":
                print("{:^75}\n\n".format("Game rules"))
                print(emoji_check, " - Objective : To earn the most points")
                print(emoji_check, " - Process : Choose a game board (triangle, circle or diamond) and choose between the two game modes : ")
                print(emoji_mode_de_jeu, "Game mode : random ==> 1, 2 or 3 random blocks are proposed to you")
                print(emoji_mode_de_jeu, "Game mode :  all   ==> You have the choice of all the blocks affiliated to the board")
                print(emoji_check, " - Place the block from its coordinates at the bottom left")
                print(emoji_check, " - You have {} chances (mode {})".format(difficulte, mode_diff))
                print(emoji_check, " - For the difficulties, if you choose the random blocks, the number of blocks differs : ")
                print(emoji_jeu_2, "| {:^5} | : 3 blocks".format("Easy"))
                print(emoji_jeu_2, "| {:^5}  | : 3 blocks".format("Medium"))
                print(emoji_jeu_2, "| {:^5}  | : 2 blocks".format("Hard"))
                print(emoji_jeu_2, "| {:^5}  | : 1 block".format("God"))


            self.display()
        ##

        #Generic
        if self.choice_user == '3':
            print("\n\n\n")
            if language =="fr":
                print("{:^75}\n\n".format("Collaborateurs"))
            elif language == "en":
                print("{:^75}\n\n".format("Collaborators"))
            lst_author = ["Valentin Menon","Joss Douniama Okana"]
            print("{} {:^25} {}".format(emoji_valentin, lst_author[0], emoji_valentin))
            print("{} {:^25} {}".format(emoji_joss, lst_author[1], emoji_joss))
            self.display()
        ##

        #Settings
        if self.choice_user == '4':
            if language == "fr":
                print("\n")
                print("{} {:^5} {}".format(emoji_setting, "  Vous êtes dans les paramètres", emoji_setting))

                print("Options : \n")
                print("1 - {}  Changer la difficulté".format(emoji_diff))
                print("2 - {} Changer la langue".format(emoji_flag))
                print("3 - {} Menu".format(emoji_bad))

                self.choice_user_para = input("Faire votre choix (1, 2, 3) : ")
                while self.choice_user_para < '1' or self.choice_user_para > '3':
                    self.choice_user_para = input("Faire votre choix (1, 2, 3) : ")

            elif language == "en":
                print("\n")
                print("{} {:^5} {}".format(emoji_setting, "  You are in the settings", emoji_setting))

                print("Features : \n")
                print("1 - {}  Change the difficulty".format(emoji_diff))
                print("2 - {} Change language".format(emoji_flag))
                print("3 - {} Menu".format(emoji_bad))

                self.choice_user_para = input("Make your choice (1, 2, 3) : ")
                while self.choice_user_para < '1' or self.choice_user_para > '3':
                    self.choice_user_para = input("Make your choice (1, 2, 3) : ")

            #Difficulty
            if self.choice_user_para == '1':
                if language == "fr":
                    print("\n")
                    print("1 - {} {:^10} {}   (5 erreurs possibles)".format(emoji_diff_1, "Facile", emoji_diff_1))
                    print("2 - {} {:^10} {}   (3 erreurs possibles)".format(emoji_diff_2, "Moyen ",  emoji_diff_2))
                    print("3 - {} {:^10} {}   (1 erreur  possible )".format(emoji_diff_3, "Dur   ",    emoji_diff_3))
                    print("4 - {} {:^10} {}   (Aucune chance)      ".format(emoji_diff_4, "God   ",    emoji_diff_4))
                    print("5 - {} {:^10} {}                        ".format(emoji_bad,    "Menu   ",    emoji_bad))

                    self.choice_user_para_diff = input("Faire votre choix (1, 2, 3, 4, 5) : ")
                    while self.choice_user_para_diff < '1' or self.choice_user_para_diff > '5':
                        self.choice_user_para_diff = input("Faire votre choix (1; 2, 3, 4, 5) : ")
                
                elif language == "en":
                    print("\n")
                    print("1 - {} {:^10} {}   (5 possible errors)".format(emoji_diff_1, "Easy", emoji_diff_1))
                    print("2 - {} {:^10} {}   (3 possible errors)".format(emoji_diff_2, "Medium ",  emoji_diff_2))
                    print("3 - {} {:^10} {}   (1 possible error )".format(emoji_diff_3, "Hard   ",    emoji_diff_3))
                    print("4 - {} {:^10} {}   (No chance)        ".format(emoji_diff_4, "God   ",    emoji_diff_4))
                    print("5 - {} {:^10} {}                      ".format(emoji_bad,    "Menu   ",    emoji_bad))

                    self.choice_user_para_diff = input("Make your choice (1, 2, 3, 4, 5) : ")
                    while self.choice_user_para_diff < '1' or self.choice_user_para_diff > '5':
                        self.choice_user_para_diff = input("Make your choice (1; 2, 3, 4, 5) : ")



                
                if self.choice_user_para_diff == '1':
                    Rule_of_the_game.display(self, 5, "Facile")
                elif self.choice_user_para_diff == '2':
                    Rule_of_the_game.display(self, 3, "Moyen")
                elif self.choice_user_para_diff == '3':
                    Rule_of_the_game.display(self, 2, "Dur")
                elif self.choice_user_para_diff == '4':
                    Rule_of_the_game.display(self, 1, "God")
                elif self.choice_user_para_diff == '5':
                    Rule_of_the_game.display(self)
                else:
                    Rule_of_the_game.display(self)
            #    

            #Change language
            if self.choice_user_para == '2':
                

                if language == "fr":
                    print("1 - {} Français".format(emoji_fr))
                    print("2 - {} Anglais".format(emoji_en))
                    self.choice_user_para_lang = input("Faire votre choix (1, 2) : ")
                    while self.choice_user_para_lang < '1' or self.choice_user_para_lang > '2':
                        self.choice_user_para_lang = input("Faire votre choix (1, 2) : ")

                elif language == "en":
                    print("1 - {} French".format(emoji_fr))
                    print("2 - {} English".format(emoji_en))
                    self.choice_user_para_lang = input("Make your choice (1, 2) : ")
                    while self.choice_user_para_lang < '1' or self.choice_user_para_lang > '2':
                        self.choice_user_para_lang = input("Make your choice (1, 2) : ")

                if self.choice_user_para_lang == '1':
                    Rule_of_the_game.display(self, difficulte, mode_diff, "fr", nb_colonne)
                elif self.choice_user_para_lang == '2':
                    Rule_of_the_game.display(self, difficulte, mode_diff, "en", nb_colonne)
                # --- Ajouter des langues ici --- #
                else:
                    print("Contact admin : error 'language' ")
                    Rule_of_the_game(self)

            #

            
            elif self.choice_user_para == '3':
                Rule_of_the_game.display(self)
            
            else:
                print("Contact admin : error 'Parametre'")
        
        else:
            Rule_of_the_game.display(self)
        ##


    ####


    #Block Selection User Policy
    def user_policy(self, emoji_alea, emoji_tous, language):
        ### Intialize the user policy
        ##### emoji_alea, emoji_tous : emoji

        emoji_bad = "\u274E"

        if language == "fr":
            print("\nVous avez le choix entre deux suggestion de blocs :")
            print("1 - {}  Affichage de l'ensemble des blocs du jeu".format(emoji_tous))
            print("2 - {} Affichage de 3 blocs aléatoires".format(emoji_alea))
            print("3 - {} Menu".format(emoji_bad))
            self.choice_user_politique_suggestion = input("Faite votre choix (1, 2, 3): ")
            while self.choice_user_politique_suggestion < '1' or self.choice_user_politique_suggestion > '3':
                self.choice_user_politique_suggestion = input("Faite votre choix (1, 2, 3): ")
            
        elif language == "en":
            print("\nYou can choose between two suggestions of blocks :")
            print("1 - {}  Display of all the blocks in the game".format(emoji_tous))
            print("2 - {} Display of 3 random blocks".format(emoji_alea))
            print("3 - {} Menu".format(emoji_bad))
            self.choice_user_politique_suggestion = input("Make your choice (1, 2, 3): ")
            while self.choice_user_politique_suggestion < '1' or self.choice_user_politique_suggestion > '3':
                self.choice_user_politique_suggestion = input("Make your choice (1, 2, 3): ")
        
        if self.choice_user_politique_suggestion == '3':
            Rule_of_the_game.display(self)
        
    def user_policy_2(self, figure_1_suggestion, figure_2_suggestion, path_figure, vide, plein, target, min, maj, bad, good, diff, language):
        ### Preserve user policy settings during gameplay
        ##### figure_1_suggestion : one of the shape group
        ##### figure_2_suggestion : the other shape group
        ##### path_figure         : path to the .txt where all the blocks are
        ##### vide  : empty slot
        ##### plein : full slot
        ##### target, min, maj, bad, good : emoji
        ##### diff  : difficulty 


        if self.choice_user_politique_suggestion == '1':
            Figure_placement.placement_bloc_all(self, figure_1_suggestion, figure_2_suggestion, path_figure, vide, plein, target, min, maj, bad, good, diff, language)
        if self.choice_user_politique_suggestion == '2':
            #number of blocks placed according to the difficulty
            if diff >= 3: 
                Figure_placement.placement_bloc_alea(self, figure_1_suggestion, figure_2_suggestion, 3, vide, plein, target, min, maj, bad, good, diff, language)
            elif diff == 2:
                Figure_placement.placement_bloc_alea(self, figure_1_suggestion, figure_2_suggestion, 2, vide, plein, target, min, maj, bad, good, diff, language)
            elif diff == 1:
                Figure_placement.placement_bloc_alea(self, figure_1_suggestion, figure_2_suggestion, 1, vide, plein, target, min, maj, bad, good, diff, language)
            else:
                print("Contact admin : error 'policy_suggestion'")
        else:
            Rule_of_the_game.display(self)
    ####
                
    #Return function for other class
    def return_choice_user_tray(self):
        return self.choice_user_plateau
    ####
    

    #display of points
    def point_display(self, language):
        ### Display the user points

        emoji_ligne_horizontal = '\U00002550'

        if language == "fr":
            print("\n", 10*emoji_ligne_horizontal)
            print("Vous avez {} points".format(Point.return_point(self)))
            print("",10*emoji_ligne_horizontal, "\n")

        elif language == "en":
            print("\n", 10*emoji_ligne_horizontal)
            print("You have {} points".format(Point.return_point(self)))
            print("",10*emoji_ligne_horizontal, "\n")
    ####

    #Player Odds Display
    def remaining_chance(self, diff, language):
        ### Displays the user's chance number before defeat
        ##### diff : difficulty 

        emoji_fin = "\u2728"
        emoji_champion = "\U0001f3c6"
        emoji_force = "\u270A"

        if language == "fr":
            middle = " Continue, tu as fait " + str(Figure_placement.return_error_point(self)) + " erreurs . Il te reste " + str(diff-Figure_placement.return_error_point(self)) + " chances"

            if Figure_placement.return_error_point(self) == 0:
                print("{} {:^10} {}".format(emoji_champion, " Champions, Aucune erreur, il te reste tous tes coups", emoji_champion))
            if Figure_placement.return_error_point(self) > 0 and Figure_placement.return_error_point(self) < diff:
                print("{} {:^10} {}".format(emoji_force, middle, emoji_force))
            if Figure_placement.return_error_point(self) == diff:
                print("{} {:^10} {}".format(emoji_fin, " C'est fin de carrière pour toi mon ami, la partie est fini", emoji_fin))
                Rule_of_the_game.display(self)
            
        elif language == "en":
            middle = " Go on, you've made " + str(Figure_placement.return_error_point(self)) + " mistakes. You have " + str(diff-Figure_placement.return_error_point(self)) + " chances left"

            if Figure_placement.return_error_point(self) == 0:
                print("{} {:^10} {}".format(emoji_champion, " Champions, No mistakes, you still have all your moves", emoji_champion))
            if Figure_placement.return_error_point(self) > 0 and Figure_placement.return_error_point(self) < diff:
                print("{} {:^10} {}".format(emoji_force, middle, emoji_force))
            if Figure_placement.return_error_point(self) == diff:
                print("{} {:^10} {}".format(emoji_fin, " It's the end of your career my friend, game over", emoji_fin))
                Rule_of_the_game.display(self)


    ####




if __name__ == "__main__":
    Rule_of_the_game().display()
    
