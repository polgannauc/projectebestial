# Mòdul per establir els elementes i les seves regles

import var_globals
import random


def generar_posicions(mida, dicc_elements):
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)] # Generem totes les posicions possibles
    random.shuffle(combinacions_possibles) # Les barrejem

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
    efectes = {
            1: {'A': 20, 'L': 5, 'R': 100, 'T': 20, 'C': 30},
            2: {'A': 15, 'L': 5, 'R': 50,  'T': 25, 'C': 40},
            3: {'A': 10, 'L': 2, 'R': 25,  'T': 30, 'C': 50}
            }
    
    #Diccionari per escollir la vida màxima segons el nivell
    vida_maxima = {1:100, 2:50, 3:25}[nivell]

    if simbol in efectes[nivell]:
        if simbol in ["A","L","R"]:
            if simbol == "L" and dicc_inventari["ampolla"] == 2: # És un llac i l'ampolla està buida
                dicc_inventari["ampolla"] = 1 # S'omple l'ampolla
                print("\nHas omplert l'ampolla al llac!")
            elif simbol != "L" or dicc_inventari["ampolla"] != 1: # No és un llac o l'ampolla no està plena
                # Establim la vida màxima amb la funció min, que ens retornarà el valor més petit
                var_globals.jugador_vida = min(var_globals.jugador_vida + efectes[nivell][simbol], vida_maxima)
            if simbol == "A":
                var_globals.comptador_animals += 1
        else:
            if simbol == "T" and dicc_inventari["ganivet"] == 1: # És una trampa i el ganivet està preparat
                print("\nHas desactivat la trampa amb el ganivet!")
                dicc_inventari["ganivet"] = 0
                elements[x][y] = '·'
            elif simbol != "T" or dicc_inventari["ganivet"] != 1: # O no és una trampa o el ganivet no està preparat
                var_globals.jugador_vida -= efectes[nivell][simbol]
        if simbol != "T":
            elements[x][y] = '·' # Eliminem la resta d'elements excepte la trampa
    return elements

# La regla de la fada només s'implementa en els nivells 2 i 3
def tocar_fada(elements):
    x,y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]
    if simbol == "F":
        print("\nHas trobat una fada! El mapa serà revelat durant 5 torns!")
        var_globals.visio_completa = 5 # Comptador de visió completa
        elements[x][y] = "·"  # Eliminem l'element del mapa
    return(elements)


# Falta implementar mecanica del inventari i els objecte, però com no se si tindrem temps, ho deixo comentat
def mostrar_inventari(dicc_inventari):
    estats_ampolla = {
        3: "1. Ampolla buida",
        2: "1. Omplir aigua d'un llac",
        1: "1. Beure ampolla d'aigua",
        0: "1. Ja has fet servir l'ampolla"
    }
    estats_ganivet = {
        2: "2. Preparar ganivet",
        1: "2. El ganivet està preparat",
        0: "2. Ja has fet servir el ganivet"
    }
    
    print("\nTens els següents objectes en l'inventari:")
    
    # Mostrar ampolla i ganivet amb els diccionaris d'estats
    print(f"\n\t{estats_ampolla.get(dicc_inventari['ampolla'], '1. Estat desconegut')}")
    print(f"\n\t{estats_ganivet.get(dicc_inventari['ganivet'], '2. Estat desconegut')}")
    
    print("\n\t3. No fer res")

def utilitzar_objecte(eleccio, dicc_inventari):
    nivell = var_globals.level
    vida_maxima = {1: 100, 2: 50, 3: 25}[nivell]

    if eleccio == 1: # Ampolla
        if dicc_inventari["ampolla"] == 3:
            dicc_inventari["ampolla"] = 2
        if dicc_inventari["ampolla"] == 2:
            print("\nAmpolla preparada per fer servir. Omple-la en un llac (L).")
        elif dicc_inventari["ampolla"] == 1:  # Si està plena, la beus
            var_globals.jugador_vida = min(var_globals.jugador_vida + 5, vida_maxima)
            dicc_inventari["ampolla"] = 0  # Ampolla gastada
            print("\nHas begut l'aigua de l'ampolla i t'has curat 5 punts de vida!")
        else:
            print("\nJa has fet servir l'ampolla.")
    elif eleccio == 2:  # Ganivet
        if dicc_inventari["ganivet"] == 2:  # Si està sense preparar, el prepares
            dicc_inventari["ganivet"] = 1
            print("\nHas preparat el ganivet. Ara pots desactivar una trampa!")
        elif dicc_inventari["ganivet"] == 1:
            print("\nEl ganivet ja està preparat.")
        else:
            print("\nJa has fet servir el ganivet.")
    else:
        pass
    return dicc_inventari