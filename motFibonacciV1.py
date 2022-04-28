# -*- coding: utf-8 -*-
"""
@author: Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion

@description : ce fichier contient le code générant le mot de fibonacci et un algorithme permettant de modéliser une fractale à partir de ce mot
"""
#module pour dessiner la fractale progressivement
from turtle import *

#méthode non récursive pour générer le mot de fibonnacci
def motFibonacci(n):
    s="0"
    s2="01"
    #variable permettant de stocker la chaine au rang n-1
    tmp=""
    #on construit la chaine en la concaténant avec la chaine au rang n-2 et n-1
    for i in range(2,n):
        tmp=s2
        s2+=s
        s=tmp
    return s2

#méthode récursive
def motFibo(n):
    #lorsqu'on arrive au rang n-1
    if(n==1):
        return '0'
    #lorsqu'on arrive au rang n-2
    if(n==0):
        return '1'
    #on renvoit une chaine implémentée de manière récursive en appelant la fonction pour les valeurs à n-2 et n-1
    return motFibo(n-1) + motFibo(n-2)

#dessin de la fractale à l'aide du module turtle
def dessin():
    #couleurs du curseur
    color('red', 'yellow')
    #on stocke le mot de fibonacci généré à l'aide de la fonction ci-dessus dans la liste fib
    fib = motFibo(2)    
    #on affiche le mot de fibonacci (cette ligne peut être supprimée, elle permet simplement d'observer le résultat dans la console)
    print(fib)
    #variable pour parcourir la liste fib, commençant donc à l'index 0
    rang=0
    #longueur d'un trait
    pas=2
    
    left(90)
    forward(pas)
    #si on arrive à la fin de la liste on sort de la boucle
    while rang!=len(fib):
        #si la chiffre est 1
        if fib[rang] == "1":
            #on avance
            forward(pas)
        else:
            #sinon si le rang de ce chiffre dans la liste est pair
            if (rang%2)==0:
                #on tourne à droite puis on avance
                right(90)
                forward(pas)
            #sinon on tourne à gauche et on avance
            else:
                left(90)
                forward(pas)
        rang+=1#on passe à l'élément suivant de la liste

    done()


dessin()
