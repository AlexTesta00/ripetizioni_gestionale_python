# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:23:11 2023

@author: Alecs
"""

#Metodo Veloce
potenza = lambda x : x*x
print(potenza(0))

#Metodo Prolisso
def funzione_potenza(number):
    if(number == 0):
        return 1
    else:
        return number*number

print(funzione_potenza(0))

#Ricorsione :(
def calcola_potenza(base, esponente):
    if esponente == 0:
        return 1
    elif esponente < 0:
        return 1 / calcola_potenza(base, -esponente)
    else:
        return base * calcola_potenza(base, esponente - 1)

print(calcola_potenza(2, 2))