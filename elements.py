import var_globals
import random

dic_pos = {}

# Funció per generar un diccionari amb cada element com a clau i els valors com llistes de tuples amb les posicions
# Accepta com a paràmetres: mida del mapa, llista amb els elements, diccionari amb quantitat de cada element segons el nivell

def generar_posicions(mida, ll, diccionari):
    global dic_pos
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)]
    random.shuffle(combinacions_possibles)
    pos_jugador = combinacions_possibles.pop()
    var_globals.jugador_x = pos_jugador[0]
    var_globals.jugador_y = pos_jugador[1]
    for i in ll:
        ll_aux = []
        for j in range(diccionari[i]):
            ll_aux.append(combinacions_possibles.pop())
        dic_pos[i]=ll_aux
    return dic_pos

def elements():
    for clau, valors in dic_pos:
        for valor in valors:
            print(clau)