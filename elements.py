import var_globals
import random

dic_pos = {}

def animal():
    if var_globals.level == 1:
        max_vida = 100
    elif var_globals.level == 2:
        max_vida = 50
    elif var_globals.level == 3:
        max_vida = 25

    if var_globals.jugador_x and var_globals.jugador_y == var_globals.ll_elements['A']:
        if var_globals.jugador_vida >= max_vida:
                var_globals.jugador_vida = max_vida
        elif var_globals.jugador_vida < max_vida:
            match var_globals.level:
                case 1:
                    var_globals.jugador_vida += 20
                case 2:
                    var_globals.jugador_vida += 15
                case 3:
                    var_globals.jugador_vida += 10

def llac():
    return llac

def trampa():
    return trampa

def rei():
    return rei

def refugi():
    return refugi



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

def main():
    return main()


if __name__ == "__main__":
    main()