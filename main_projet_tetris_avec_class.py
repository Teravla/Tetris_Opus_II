import random as rd

'''
Programme Tetris L1 BN EFREI
'''


#path = input("Spécifier le chemin d'accès à la figure: ")

programme = open("C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt", "w")
#"C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\programme.txt"





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
                chiffre = str(chiffre_donné)+"  "
                grille_2.append(chiffre)
            self.grille.append(grille_2)
            grille_2 = []
        return self.grille
    
    def read_grid(self):
        programme.write('    ')
        for k in range(len(self.lst_lettre_min)):
            programme.write(self.lst_lettre_min[k])
            programme.write('  ')
        programme.write('\n   ')
        programme.write(int(self.nb_colonne)*3*'-'+'-')
        programme.write('\n')
        for i in range(int(self.nb_colonne)):
            programme.write(self.lst_lettre_maj[i])
            programme.write(" | ")
            for j in range(len(self.grille[i])):
                programme.write(str(self.grille[i][j]))
            programme.write("|")
            programme.write("\n")
        programme.write('   ')
        programme.write(int(self.nb_colonne)*3*'-'+'-')


    def return_grille(self):
        return self.grille
    def return_majuscule(self):
        return self.lst_lettre_maj
    def return_minuscule(self):
        return self.lst_lettre_min


    
    #Affichage des lettres
    def lettre_min(self):
        lim = 97+int(int(self.nb_colonne))
        for i in range(97, lim):
            lettre_min = chr(i)
            lettre = lettre_min
            self.lst_lettre_min.append(lettre)
        
        return self.lst_lettre_min
    
    def lettre_maj(self):
        self.lst_lettre_minuscule = []
        lim = 65+int(int(self.nb_colonne))
        for i in range(65, lim):
            lettre_maj = chr(i)
            lettre = lettre_maj
            self.lst_lettre_maj.append(lettre)

        return self.lst_lettre_maj
    #FIn Affichage des Lettres
    
    #Figures
    def figure_triangle(self):
        min = int(self.nb_colonne)//2
        max = (int(self.nb_colonne)//2)+1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min -= 1
            max += 1

    def figure_losange(self):
        min = int(self.nb_colonne)//2
        max = (int(self.nb_colonne)//2)+1
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min -= 1
            max += 1
        min = 0
        max = int(self.nb_colonne)
        for i in range(int(self.nb_colonne)//2,int(self.nb_colonne)-1):
            for j in range(min, max):
                self.grille[i][j] = '1  '
            min += 1
            max -= 1
        self.grille[int(self.nb_colonne)-1][int(self.nb_colonne)//2] = '1  '
    
    def figure_cercle(self, trou):
        #Haut Gauche
        max = int(self.nb_colonne)//4
        min = 0
        for i in range(max):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            max-=1
        #Haut Droit
        max = int(self.nb_colonne)
        min = int((3/4)*int(self.nb_colonne)+1)
        for i in range(int(self.nb_colonne)//4):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            min+=1
        #Bas Gauche
        max = int(self.nb_colonne)//4
        min = 1
        for i in range(int((3/4)*int(self.nb_colonne)+1),int(self.nb_colonne)):
            for j in range(min):
                self.grille[i][j] = str(trou)+'  '
            min+=1
        #Bas Droit
        max = int(self.nb_colonne)
        min = int(self.nb_colonne)
        for i in range(int((3/4)*int(self.nb_colonne)+1),int(self.nb_colonne)):
            for j in range(min, max):
                self.grille[i][j] = str(trou)+'  '
            min-=1
    #Fin Figures



class Forme:

    def __init__(self):
        pass
    
    def formes_tous(self):
        self.forme_tous_ensemble = []
        self.forme_tous_1= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]
        self.forme_tous_2= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,0,0,0]]
        self.forme_tous_3= [[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
        self.forme_tous_4= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,1,0,0]]
        self.forme_tous_5= [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]
        self.forme_tous_6= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0]]
        self.forme_tous_7= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0]]
        self.forme_tous_8= [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0]]
        self.forme_tous_9= [[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
        self.forme_tous_10=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0]]
        self.forme_tous_11=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0]]
        self.forme_tous_12=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]
        self.forme_tous_13=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[1,1,1,0,0]]
        self.forme_tous_14=[[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]
        self.forme_tous_15=[[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0]]
        self.forme_tous_16=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,0],[0,1,0,0,0]]
        self.forme_tous_17=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,1,0,0,0]]
        self.forme_tous_18=[[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]
        self.forme_tous_19=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0]]
        self.forme_tous_20=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]
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
        self.forme_triangle_1= [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0]]
        self.forme_triangle_2= [[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0]]
        self.forme_triangle_3= [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[1,1,1,0,0],[1,0,0,0,0]]
        self.forme_triangle_4= [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,1,0,0,0],[1,1,0,0,0]]
        self.forme_triangle_5= [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0]]
        self.forme_triangle_6= [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]]
        self.forme_triangle_7= [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
        self.forme_triangle_8= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,0]]
        self.forme_triangle_9= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
        self.forme_triangle_10=[[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[0,1,0,0,0]]
        self.forme_triangle_11=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0]]
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
        self.forme_losange_1= [[0,0,0,0,0],[0,0,0,1,1],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0]]
        self.forme_losange_2= [[0,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1]]
        self.forme_losange_3= [[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
        self.forme_losange_4= [[0,0,0,0,0],[1,1,1,1,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0]]
        self.forme_losange_5= [[0,0,0,0,0],[1,0,0,1,0],[0,1,1,0,0],[0,1,1,0,0],[1,0,0,1,0]]
        self.forme_losange_6= [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
        self.forme_losange_7= [[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1]]
        self.forme_losange_8= [[0,0,0,0,1],[0,0,0,1,1],[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0]]
        self.forme_losange_9= [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
        self.forme_losange_10=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
        self.forme_losange_11=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,1,1,0],[0,0,0,1,0]]
        self.forme_losange_12=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0]]
        self.forme_losange_13=[[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
        self.forme_losange_14=[[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]
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
        self.forme_cercle_1= [[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
        self.forme_cercle_2= [[0,0,0,0,0],[0,1,1,0,0],[1,1,1,1,0],[1,1,1,1,0],[0,1,1,0,0]]
        self.forme_cercle_3= [[0,0,0,0,0],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,0]]
        self.forme_cercle_4= [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0]]
        self.forme_cercle_5= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,0,0]]
        self.forme_cercle_6= [[0,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,0,0]]
        self.forme_cercle_7= [[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0]]
        self.forme_cercle_8= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[1,1,1,1,0]]
        self.forme_cercle_9= [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
        self.forme_cercle_10=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
        self.forme_cercle_11=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,0,0,0,1]]
        self.forme_cercle_12=[[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,1,0],[1,1,1,1,0]]
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
        self.path_figure = "C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"#input("Spécifier le chemin d'accès aux figures possible lors de votre jeu : ")

    def affichage_figure_write(self, figure):
        #"C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"
        test_affichage_figure = open(self.path_figure,"w")
        for i in range(len(figure)):
            for j in range(len(figure[i])):
                for k in range(len(figure[i][j])):
                    if figure[i][j][k]%2==1:
                        test_affichage_figure.write("- ")
                    elif figure[i][j][k]%2==0:
                        test_affichage_figure.write("0 ")
                test_affichage_figure.write('\n')
            test_affichage_figure.write('\n')

    def affichage_figure_append(self, figure):
        #"C:\\Users\\User\\Documents\\Document\\EFREI\\L1\\Info\\Projet\\test_figure.txt"
        test_affichage_figure = open(self.path_figure,"a")
        for i in range(len(figure)):
            for j in range(len(figure[i])):
                for k in range(len(figure[i][j])):
                    if figure[i][j][k]%2==1:
                        test_affichage_figure.write("- ")
                    elif figure[i][j][k]%2==0:
                        test_affichage_figure.write("0 ")
                test_affichage_figure.write('\n')
            test_affichage_figure.write('\n')



class Placement_figure:
    def __init__(self) -> None:
        Forme.__init__(self)
        Grille.__init__(self)


    #Choix de la politique de suggestion
    def blocs_alea(self,figure_1,figure_2,nb_blocs_afficher):
        self.lst_alea=[]
        self.lst_affichage_forme=[]
        self.lst_forme_reutilisable = []

        for i in range(len(figure_1)):
            self.lst_alea.append(figure_1[i])
        for i in range(len(figure_2)):
            self.lst_alea.append(figure_2[i])

        #CONDITION A CHANGER#
        for i in range(1):

            print("\nVoici les choix que vous avez pour 'Affichage de 3 blocs aléatoire' : \n")

            for i in range(nb_blocs_afficher):
                #Création du nombre aléatoire
                nb_alea = rd.randint(0,len(self.lst_alea)-1)
                
                self.lst_affichage_forme.append(self.lst_alea[nb_alea])
                self.lst_forme_reutilisable.append(self.lst_alea[nb_alea])
                #Suppression pour éviter la redondance
                del self.lst_alea[nb_alea]
                
                #Affichage de la forme
                for i in range(len(self.lst_affichage_forme)):
                    for j in range(len(self.lst_affichage_forme[i])):
                        for k in range(len(self.lst_affichage_forme[i][j])):
                            if self.lst_affichage_forme[i][j][k]%2==1:
                                print("-",end=" ")
                            elif self.lst_affichage_forme[i][j][k]%2==0:
                                print("0",end=" ")
                        print('\n')
                print('\n')
                del self.lst_affichage_forme[i]
            print('\n')
        
        return self.lst_forme_reutilisable
    
    def blocs_tous(self,figure_1,figure_2):
        Forme.path_figure(self)
        Forme.affichage_figure_write(self,figure_1)
        Forme.affichage_figure_append(self,figure_2)
        print("\nLes figures possibles sont dans le fichier que vous avez spécifiez\n")
    #FIN# Choix de la politique de suggestion

    #Placement du bloc
    def placement_bloc_alea(self):

        self.placement_possible = False
        self.placement_impossible = False

        print("\nChoississez un bloc")
        choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut :")
        while choice_user_placement_bloc_alea<'1' or choice_user_placement_bloc_alea>'3':
            choice_user_placement_bloc_alea = input("1, 2 ou 3 en partant du haut :")
        
        if choice_user_placement_bloc_alea == '1':
            forme = self.lst_forme_reutilisable[0]
        if choice_user_placement_bloc_alea == '2':
            forme = self.lst_forme_reutilisable[1]
        if choice_user_placement_bloc_alea == '3':
            forme = self.lst_forme_reutilisable[2]

        print("choisir les coordonnées pour poser votre bloc :")
        print(Grille.lettre_min(self))
        print(Grille.lettre_maj(self))
        self.cordonnees_minuscule = str(input("Première coordonnée : "))
        while self.cordonnees_minuscule not in Grille.lettre_min(self):
            self.cordonnees_minuscule = str(input("Première coordonnée : "))
        self.cordonnees_majuscule = str(input("Seconde coordonnée : "))
        while self.cordonnees_majuscule not in Grille.lettre_maj(self):
            self.cordonnees_majuscule = str(input("Seconde coordonnée : "))

        grille = Grille.return_grille(self)
        lst_min = Grille.return_minuscule(self)
        lst_maj = Grille.return_majuscule(self)
        index_lst_maj = lst_maj.index(self.cordonnees_majuscule)-4
        index_lst_min = lst_min.index(self.cordonnees_minuscule)
        print(index_lst_min,index_lst_maj,end="\n\n\n")

        for i in range(len(forme)):
            for j in range(len(forme[i])):
                print(forme[i][j],end="")
            print('\n')
        
        for i in range(5):
            for j in range(5):
                #print(i,j)
                print(grille[index_lst_maj+i][index_lst_min+j],end="")
                #print(index_lst_maj-i,index_lst_min+j,end="")
            print('\n')


        for i in range(5):
            for j in range(5):
                print(forme[j][i],",",grille[index_lst_maj+i][index_lst_min+j])
                
                if forme[i][j] == 1 and grille[index_lst_maj+i][index_lst_min+j] == '1  ':
                    print("gooood pour 1 1 ")
                    self.placement_possible = True
                    print(self.placement_possible,self.placement_impossible)
                elif forme[i][j] == 1 and grille[index_lst_maj+i][index_lst_min+j] == '.  ':
                    print("gooood pour 1 . ")
                    self.placement_impossible = True
                    print(self.placement_possible,self.placement_impossible)
                elif forme[i][j] == 0 and grille[index_lst_maj+i][index_lst_min+j] == '1  ':
                    print("gooood pour 0 1 ")
                    self.placement_possible = True
                    print(self.placement_possible,self.placement_impossible)
                elif forme[i][j] == 0 and grille[index_lst_maj+i][index_lst_min+j] == '.  ':
                    print("gooood pour 0 . ")
                    self.placement_possible = True
                    print(self.placement_possible,self.placement_impossible)
            print('\n')
        
        if self.placement_impossible == True or self.placement_possible == False:
            print("Vous ne pouvez pas poser ce bloc ici")
        elif self.placement_impossible == False and self.placement_possible == True:
            print("Vous pouvez placer ce bloc ici")
        
        



    


class Regle_du_jeu:
    def __init__(self) -> None:
        Grille.__init__(self)
        Forme.__init__(self)
        Placement_figure.__init__(self)
        self.nb_colonne = 0
    
    def affichage(self):
        print("1 - Commmencer à jouer")
        print("2 - Afficher les règles du jeu")
        self.choice_user = input("Faire votre choix (1, 2) : ")
        while self.choice_user<'1' or self.choice_user>'2':
            self.choice_user = input("Faire votre choix (1, 2) : ")

        if self.choice_user == '1':
        
            self.nb_colonne = input("\nDonner le taille de votre tableau (21, 23 ou 25) : ")
            while (self.nb_colonne!='21' and self.nb_colonne!='23') and self.nb_colonne!='25':
                self.nb_colonne = input("Donner le taille de votre tableau (21, 23 ou 25) : ")
        

            print("\nChoississez votre plateau de jeu :")
            print("1 - Triangle")
            print("2 - Losange")
            print("3 - Cercle")
            self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")
            while self.choice_user_plateau<'1' or self.choice_user_plateau>'3':
                self.choice_user_plateau = input("Faire votre choix (1, 2, 3) : ")
            
            if self.choice_user_plateau == '1': #Triangle
                Grille.create_grid(self, '0', int(self.nb_colonne))
                Grille.lettre_min(self)
                Grille.lettre_maj(self)
                Grille.figure_triangle(self)
                Grille.read_grid(self)
                self.politique_suggestion_blocs(Forme.formes_triangle(self),Forme.formes_tous(self))
                Placement_figure.placement_bloc_alea(self)

            if self.choice_user_plateau == '2': #Losange
                Grille.create_grid(self, '.', int(self.nb_colonne))
                Grille.lettre_min(self)
                Grille.lettre_maj(self)
                Grille.figure_losange(self)
                Grille.read_grid(self)
                self.politique_suggestion_blocs(Forme.formes_losange(self),Forme.formes_tous(self))
                Placement_figure.placement_bloc_alea(self)

            if self.choice_user_plateau == '3': #Cercle
                Grille.create_grid(self, 1, int(self.nb_colonne))
                Grille.lettre_min(self)
                Grille.lettre_maj(self)
                Grille.figure_cercle(self, '0')
                Grille.read_grid(self)
                self.politique_suggestion_blocs(Forme.formes_cercle(self),Forme.formes_tous(self))
                Placement_figure.placement_bloc_alea(self)
        
        if self.choice_user == '2': 
            #Mettre les règle ici
            print()

    
    def politique_suggestion_blocs(self,figure_1_suggestion,figure_2_suggestion):
        print("\nVous avez le choix entre deux suggéstion de blocs :")
        print("1 - Affichage de l'ensemble des blocks du jeu")
        print("2 - Affichage de 3 blocs aléatoires")
        self.choice_user_politique_suggestion = input("Faite votre choix : ")
        while self.choice_user_politique_suggestion<'1' or self.choice_user_politique_suggestion>'2':
            self.choice_user_politique_suggestion = input("Faite votre choix : ")
        
        if self.choice_user_politique_suggestion == '1':
            Placement_figure.blocs_tous(self,figure_1_suggestion, figure_2_suggestion)
        if self.choice_user_politique_suggestion == '2':
            Placement_figure.blocs_alea(self,figure_1_suggestion,figure_2_suggestion,3)
    
    


if __name__ == "__main__":
    Regle_du_jeu().affichage()

    
