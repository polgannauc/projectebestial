# Mòdul per establir els elementes i les seves regles

import var_globals
import random


def generar_posicions(mida, dicc_elements):
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)] # Generem totes les posicions possibles segons la mida del mapa
    random.shuffle(combinacions_possibles) # Les barrejem per tenir els elements a l'atzar

    pos_jugador = combinacions_possibles.pop() 
    var_globals.jugador_x, var_globals.jugador_y = pos_jugador # Guardem la posició del jugador a variables globals

    dicc_posicions = {pos_jugador:"E"} # Clau: coordenada, valor: element

    for simbol, quantitat in dicc_elements.items(): # Iterem sobre el diccionari d'elements, guardant l'element i la quantitat de vegades que apareix
        for _ in range(quantitat):
            pos = combinacions_possibles.pop()
            dicc_posicions[pos] = simbol

    for pos in combinacions_possibles:
        dicc_posicions[pos] = "." # Resta de posicions del mapa buides 
    
    # Generem la matriu 2d amb un list comprehension.
    matriu_elements = [[dicc_posicions[i,j] for j in range(mida)] for i in range(mida)]
    
    return matriu_elements


def modificar_vida(elements, dicc_inventari):
    x,y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]
    nivell = var_globals.level

    # Clau = nivell, valor = diccionari (clau = element, valor = vida)
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
    vida_maxima = {1:100, 2:50, 3:25}[nivell]

    if simbol in cures[nivell]:

        # Establim la vida màxima amb la funció min, que ens retornarà el valor més petit
        var_globals.jugador_vida = min(var_globals.jugador_vida + cures[nivell][simbol],vida_maxima)
            
        if simbol == "A":
            var_globals.comptador_animals += 1

        elements[x][y] = "·"  # Eliminem l'element del mapa

    elif simbol in danys[nivell]:
       var_globals.jugador_vida -= danys[nivell][simbol]
       elements[x][y] = '·' 
    
    return elements

# La regla de la fada només s'implementa en els nivells 2 i 3
def tocar_fada(elements):
    x,y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]
    if simbol == "F":
        print("Has trobat una fada! El mapa serà revelat durant 5 torns!")
        var_globals.visio_completa = 5 # Comptador de visió completa
        elements[x][y] = "·"  # Eliminem l'element del mapa
    return(elements)


def mostrar_inventari(dicc_inventari):
    print("\nTens els següents objectes en l'invetari:")

    if dicc_inventari["ampolla"]==2:
        print("\n\t1.Omplir aigua d'un llac")
    elif dicc_inventari["ampolla"]==1:
        print("\n\t1.Beure amplla d'aigua")
    else:
        print("\n\t1.Ja has fer servir l'ampolla")

    if dicc_inventari["ganivet"]:
        print("\n\t2.Preparar ganivet")
    else:
        print("\n\t2.Ja has fet servir el ganivet")

    if dicc_inventari["encenedor"]:
        print("\n\t3.Preparar encenedor")
    else:
        print("\n\t3.Ja has fet servir l'encenedor")

def utilitzar_objecte(eleccio, dicc_inventari):
    match eleccio:
        case 1:
            dicc_inventari["ampolla"] = 1
        case 2:
            dicc_inventari["ganivet"] = True
        case 3:
            dicc_inventari["encenedor"] = True
    return dicc_inventari


