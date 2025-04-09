# Mòdul per establir els elementes i les seves regles

import var_globals
import random


# Funció que genera una matriu 2d amb els elements situats
def generar_posicions(mida, dicc_elements):
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)] # Generem totes les posicions possibles segons la mida del mapa
    random.shuffle(combinacions_possibles) # Les barrejem per tenir els elements a l'atzar

    pos_jugador = combinacions_possibles.pop() 
    var_globals.jugador_x, var_globals.jugador_y = pos_jugador # Guardem la posició del jugador a variables globals
    dicc_posicions = {"E": [pos_jugador]}

    for i in ["A","T","R","L","B","C"]:
        dicc_posicions[i]=[combinacions_possibles.pop() for j in range(dicc_elements[i])] # Afegim les posicions a cada element segon el número d'elements que toca per nivell

    dicc_posicions["·"]= combinacions_possibles # La resta de posicions són buides.

    # Ara generarem la matriu 2d a partir del diccionari(clau = element, valor = llista posicions)
    matriu_elements = []
    for i in range(mida):
        ll_aux=[]
        for j in range(mida):
            for key,value in dicc_posicions.items():
                for pos in value:
                    if pos == (i,j):
                        ll_aux.append(key)
        matriu_elements.append(ll_aux)
    
    return matriu_elements


def modificar_vida(elements):
    x,y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]

    # Clau = nivell, valor = diccionari (clau = element, valor = vida que guanya)
    cures = {
        1: {"A": 20, "L": 5, "R": 100},
        2: {"A": 15, "L": 5, "R": 50},
        3: {"A": 10, "L": 2, "R": 25}
    }

    danys = {
        1: {"T": 20, "C": 30},
        2: {"T": 25, "C": 40},
        3: {"T": 30, "C": 50}
    }
    
    #Diccionari per escollir la vida màxima segons el nivell
    vida_maxima = {1:100, 2:50, 3:25}

    if simbol in cures[var_globals.level]:
        # Entrem al primer diccionari per nivell i al segon per element per escollir el valor de vida que guanya
        var_globals.jugador_vida += cures[var_globals.level][simbol]

        # Establim la vida màxima
        var_globals.jugador_vida = min(var_globals.jugador_vida, vida_maxima[var_globals.level])
            
        if simbol == "A":
            var_globals.comptador_animals += 1 # Comptador dels animals

        elements[x][y] = "·"  # Eliminem l'element del mapa

    if simbol in danys[var_globals.level]:
       # Entrem al primer diccionari per nivell i al segon per element per escollir el valor de vida que perd
       var_globals.jugador_vida -= danys[var_globals.level][simbol]
       
       elements[x][y] = '·' # Eliminem l'element del mapa
    
    return elements