# -*- coding: utf-8 -*-
"""
@author: Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion

@description : ce fichier contient le code pour générer la fractale de fibonacci sous forme d'une image. 
Il reprend la structure du fichier motFibonacciV1 mais sans utiliser le module turtle.
Certaines fonctions semblables à celles de turtle on été recodées ici afin de faciliter la compréhencion du code
"""
#on importe les modules (PIL pour la génération d'images et math pour les fonctions de calcul)
#import math
from PIL import Image, ImageDraw

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

#fonction permettant de pivoter selon l'angle donné vers la gauche
def left(angle):
    global sens
    sens=sens-1
    if sens<0:
        sens=3

#fonction permettant de pivoter selon l'angle donné vers la droite
def right(angle):
    global sens
    sens=sens+1
    if sens>3:
        sens=0

#fonction peremttant de tracer un trait de longueur pas dans la direction sens
def forward(pas):
    global sens,shape
    cor=shape[1]
    if sens==0:
        shape=[cor,(cor[0],cor[1]-pas)]
    elif sens==1:
        shape=[cor,(cor[0]-pas,cor[1])]
    elif sens==2:
        shape=[cor,(cor[0],cor[1]+pas)]
    else:
        shape=[cor,(cor[0]+pas,cor[1])]
    img1.line(shape, fill ="white", width = 0)
    
#on définit la taille de l'image
w, h = 10000, 10000
pas=1
shape=[(0,h),(0,h+pas)]
sens=0
rang=0
# on initialise un objet de type "image"
img = Image.new("RGB", (w, h))
fib = motFibo(30)

img1 = ImageDraw.Draw(img)
img1.line(shape, fill ="white", width = 0)
#code reprenant la même strucutre que dans le fichier motFibonacciV1.py
while rang!=len(fib):
    if fib[rang] == "1":
        forward(pas)
    else:
        if (rang%2)==0:
            right(90)
            forward(pas)
        else:
            left(90)
            forward(pas)
    rang=rang+1

#on enregistre l'image
img.save("test22.png")
