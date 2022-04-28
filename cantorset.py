# -*- coding: utf-8 -*-
"""
@author: Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion

@description : ce fichier contient le code permettant de génerer le set de Cantor(une fractale) puis de l'implémenter dans un fichier et génerer une image et une musique fractales
    
"""
#fonction qui convertit une liste en chaine de caractères (afin de l'écrire dans un fichier ensuite)
def convertListToStr(ligne):
    lignestr=""
    #on convertit chaque élément du tableau en caractère qu'on ajoute à la chaine lignestr
    for i in ligne:
        lignestr+=str(i)
    return lignestr

def cantorSet(filename):
    #le fichier dans lequel on va stocker la matrice du set de cantor
    f = open(filename, "a")
    #on demande le nombre de lignes du set de cantor que l'on souhaite générer
    nbrLigne = int(input("Rentrez le nombre de ligne (min 1) : "))
    #on calcule le nombre de caracteres nécessaires par ligne soit 3 à la puissance nbrligne-1
    nbrCarac=pow(3,nbrLigne-1)
    #on génère la première ligne (une ligne remplie de 1)
    ligne=[1]*nbrCarac
    #on écrit cette ligne dans le fichier
    lignestr = convertListToStr(ligne)
    f.write(lignestr+"\n")
    #on affiche cette ligne dans la console (cette ligne peut être supprimée, elle permet simplement d'observer le résultat dans la console)
    print(ligne)
    #cette boucle tourne tant que l'on a pas dessiné toutes les lignes demandées
    for i in range(nbrLigne-2,-1, -1):
        k=(int(pow(3,i)))
        for j in range(0, nbrCarac, pow(3,i)):
            #si le rang j est impair, on va remplacer les i éléments par des 0
            if(j%2==1):    
                for i in range(0,k):
                    #on remplace l'élément par un 0
                    ligne[i+j]=0
        #on affiche la nouvelle ligne dans la console (cette ligne peut être supprimée, elle permet simplement d'observer le résultat dans la console)        
        print(ligne)
        #ecriture dans le fichier : on peut aussi convertir la liste directement à l'aide d'un join
        f.write(''.join(list(map(str,ligne)))+"\n")
    #a la fin du programme, on ferme le fichier
    f.close()
     
cantorSet("testCantor293.txt")

