# -*- coding: utf-8 -*-
"""
@author: Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion
@description : ce fichier contient le code permettant de génerer le set de Cantor(une fractale) puis de l'implémenter dans un fichier et génerer une image et une musique fractales
    
"""

from math import sin,pi
import random


#fonction qui convertit une liste en chaine de caractères (afin de l'écrire dans un fichier ensuite)
def convertListToStr(ligne):
    lignestr=""
    #on convertit chaque élément du tableau en caractère qu'on ajoute à la chaine lignestr
    for i in ligne:
        lignestr+=str(i)
    return lignestr

def cantorSet(filename, nbrLigne):
    tab = []
    #on calcule le nombre de caracteres nécessaires par ligne soit 3 à la puissance nbrligne-1
    nbrCarac=pow(3,nbrLigne-1)
    #on génère la première ligne (une ligne remplie de 1)
    ligne=[1]*nbrCarac
    #on affiche cette ligne dans la console (cette ligne peut être supprimée, elle permet simplement d'observer le résultat dans la console)
    
    #cette boucle tourne tant que l'on a pas dessiné toutes les lignes demandées
    for i in range(nbrLigne-2,-1, -1):
        k=(int(pow(3,i)))
        for j in range(0, nbrCarac, pow(3,i)):
            #si le rang j est impair, on va remplacer les i éléments par des 0
            if(j%2==1):    
                for i in range(0,k):
                    #on remplace l'élément par un 0
                    ligne[i+j]=0
        tab.append(ligne)
        #on affiche la nouvelle ligne dans la console (cette ligne peut être supprimée, elle permet simplement d'observer le résultat dans la console)        
    return tab

#fonction qui enregistre le son de la fractale de Cantor dans un fichier .wav
def fract_to_sound(filename,val):
    
    #initialisation de la taille de la partition
    N=1000
    x=range(N) 
    y=N*[0]

    #Ajout de son aléatoire entre 900 et 1000 Hz
    for i in x:
      y[i]=random.randint(900,1000)
    y=1313*y 

    #récuperation des bibliothèques nécessaires a la création d'un son avec Python
    import wave
    import struct
    
    #création du fichier .wav et configuration du son
    sound=wave.open(filename,"w")
    sound.setnchannels(1)
    sound.setsampwidth(2) 
    sound.setframerate(100000)
    sound.setcomptype('NONE','Not Compressed')
    BinStr=b'' 
    zero = 0

    #recuperation de la fractale de Cantor pour certaine valeur
    song=cantorSet("cantor.txt", val)
    
    #parcours de la fractale au format binaire pour ajouter ou non un son dans le fichier a chaque temps
    for j in song:
        for i in j:
            if i == 0  :
                BinStr = BinStr + struct.pack('h',round(0))
            else :
                BinStr = BinStr + struct.pack('h',round(y[i]))

    #ecriture dans le fichier et fermeture du fichier
    sound.writeframesraw(BinStr)
    sound.close()

print("Saisissez 'fract_to_sound(filename.wav, n)' pour créer un fichier .wav contenant le son de la fractale de cantor a l'étape n")

#création de 4 fichiers sons pour les étapes 9 a 12 de la fractale
fract_to_sound("son9.wav", 9)
fract_to_sound("son10.wav", 10)
fract_to_sound("son11.wav", 11)
fract_to_sound("son12.wav", 12)