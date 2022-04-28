# -*- coding: utf-8 -*-
"""
@author: Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion

@description : ce fichier contient le code permettant de comparer les temps d'éxécution de génération du mot de Fibonacci (la méthode récursive est plus efficace)'   
"""
#module permettant d'accéder aux temps d'éxécution
import timeit
code = """ 
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
(motFibonacci(20))   
"""

execution_time = timeit.timeit(code, number=1)

print("temps d'éxecution du code non récursif pour 20 itérations "+str(execution_time))
#méthode non récursive pour générer le mot de fibonnacci


#méthode récursive
code2 ="""
def motFibo(n):
    #lorsqu'on arrive au rang n-1
    if(n==1):
        return '0'
    #lorsqu'on arrive au rang n-2
    if(n==0):
        return '1'
    #on renvoit une chaine implémentée de manière récursive en appelant la fonction pour les valeurs à n-2 et n-1
    return motFibo(n-1) + motFibo(n-2)
(motFibo(20))
"""
execution_time = timeit.timeit(code2, number=1)

print("temps d'éxecution du code récursif pour 20 itérations "+str(execution_time))
