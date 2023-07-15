# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:05:52 2023

@author: Alecs
"""

#Creo la funzione che prende un numero e lo eleva al cubo
cube = lambda x : x**3

#Creo la lista in cui inserirò tutti i numeri elevati al cubo
#e divisibili per due
list_of_cube = []

#Prendo i numeri compresi tra 0 e 99(inclusi)
#li elevo al cubo
#se il loro cubo è divisibile per due, lo inserisco in lista, altrimenti no
for k in range(100):
    cube_number = cube(k)
    if cube_number % 2 == 0:
        list_of_cube.append(cube_number)

print(list_of_cube)