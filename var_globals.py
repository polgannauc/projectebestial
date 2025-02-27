# En aquest mòdul és on aniran les variables globals
## Exemple: amplada del mapa o energia inicial
## Altres variables que podem posar, com les posicions de l'explorador i dels element

import random

# Funció per escollir la mida del mapa segons el nivell de dificultat:
def mida_mapa(var_nivell):
    mida = None
    match var_nivell:
        case 1:
            mida = 5
        case 2:
            mida = 10
        case 3:
            mida = 15
    return mida


#Funció per generar un diccionari on cada clau és l'element i el valor la quantitat de vegades que apareix en el mapa segons dificultat
def quantitat_elements(var_nivell):
    nivells = { # Generem un diccionari, on cada nivell és la clau, i el valor un diccionari amb els elements i la quantitat
        1: {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1},
        2: {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3},
        3: {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5},
    }
    return nivells.get(var_nivell, {}) #Ens retornarà només un diccionari segons el nivell, o un diccionari buit


# Funció per generar un diccionari amb cada element com a clau i els valors com llistes de tuples amb les posicions
# Accepta com a paràmetres: mida del mapa, llista amb els elements, diccionari amb quantitat de cada element segons el nivell
def generar_posicions(mida,ll,diccionari):
    dic_pos = {}
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)]
    random.shuffle(combinacions_possibles)
    for i in ll:
        ll_aux = []
        for j in range(diccionari[i]):
            ll_aux.append(combinacions_possibles.pop())
        dic_pos[i]=ll_aux
    return dic_pos


# Funció per generar la visibilitat segons el nivell de dificultat



#Llista amb tots els elements
ll_elements = ["E","A","T","R","L","B","C"]




    
