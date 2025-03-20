import var_globals
import random

# Funció per generar un diccionari amb cada element com a clau i els valors com llistes de tuples amb les posicions
# Accepta com a paràmetres: mida del mapa, llista amb els elements, diccionari amb quantitat de cada element segons el nivell

def generar_posicions(mida, ll, diccionari):
    matriu_elements = []
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)]
    random.shuffle(combinacions_possibles)
    pos_jugador = combinacions_possibles.pop()
    var_globals.jugador_x, var_globals.jugador_y = pos_jugador
    dic_pos = {"E": [pos_jugador]}
    for i in ll:
        dic_pos[i]=[combinacions_possibles.pop() for j in range(diccionari[i])]
    dic_pos["·"]= combinacions_possibles
    for i in range(mida):
        ll_aux=[]
        for j in range(mida):
            for key,value in dic_pos.items():
                for pos in value:
                    if pos == (i,j):
                        ll_aux.append(key)
        matriu_elements.append(ll_aux)
    return matriu_elements


def animal(elements):
    for i in range(var_globals.mida):
        for j in range(var_globals.mida):
            if elements[i][j] == "A" and (i,j) == (var_globals.jugador_x,var_globals.jugador_y):
                match var_globals.level:
                    case 1:
                        var_globals.jugador_vida += 20
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 100)
                    case 2:
                        var_globals.jugador_vida += 15
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 50)
                    case 3:
                        var_globals.jugador_vida += 10
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 25)
                var_globals.comptador_animals+=1
                elements[i][j] = "·"
    return elements
                

def trampa(elements):
    for i in range(var_globals.mida):
        for j in range(var_globals.mida):
            if elements[i][j] == "T" and (i,j) == (var_globals.jugador_x,var_globals.jugador_y):
                match var_globals.level:
                    case 1:
                        var_globals.jugador_vida -= 20
                    case 2:
                        var_globals.jugador_vida -= 25
                    case 3:
                        var_globals.jugador_vida -= 30
                elements[i][j] = "·"
    return elements


def llac(elements):
    for i in range(var_globals.mida):
        for j in range(var_globals.mida):
            if elements[i][j] == "L" and (i,j) == (var_globals.jugador_x,var_globals.jugador_y):
                match var_globals.level:
                    case 1:
                        var_globals.jugador_vida += 5
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 100)
                    case 2:
                        var_globals.jugador_vida += 5
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 50)
                    case 3:
                        var_globals.jugador_vida += 2
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 25)
                elements[i][j] = "·"
    return elements

def refugi(elements):
    for i in range(var_globals.mida):
        for j in range(var_globals.mida):
            if elements[i][j] == "R" and (i,j) == (var_globals.jugador_x,var_globals.jugador_y):
                match var_globals.level:
                    case 1:
                        var_globals.jugador_vida += 100
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 100)
                    case 2:
                        var_globals.jugador_vida += 50
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 50)
                    case 3:
                        var_globals.jugador_vida += 25
                        var_globals.jugador_vida = min(var_globals.jugador_vida, 25)
                elements[i][j] = "·"
    return elements



def rei(elements):
    for i in range(var_globals.mida):
        for j in range(var_globals.mida):
            if elements[i][j] == "C" and (i,j) == (var_globals.jugador_x,var_globals.jugador_y):
                match var_globals.level:
                    case 1:
                        var_globals.jugador_vida -= 30
                    case 2:
                        var_globals.jugador_vida -= 40
                    case 3:
                        var_globals.jugador_vida -= 50
                elements[i][j] = "·"
    return elements







def main():
    return main()


if __name__ == "__main__":
    main()