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


def guanyar_vida(elements):
    x,y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]

    # Clau = nivell, valor = diccionari (clau = element, valor = vida que guanya)
    cures = {
        1: {"A": 20, "L": 5, "R": 100},
        2: {"A": 15, "L": 5, "R": 50},
        3: {"A": 10, "L": 2, "R": 25}
    }
    
    #Diccionari per la vida màxima segons el nivell
    vida_maxima = {1:100, 2:50, 3:25}

    if simbol in cures[var_globals.level]:
        # Entrem al primer diccionari per nivell i al segon per element
        var_globals.jugador_vida += cures[var_globals.level][simbol]

        # Fem servir la vida màxima
        var_globals.jugador_vida = min(var_globals.jugador_vida, vida_maxima[var_globals.level])

        if simbol == "A":
            var_globals.comptador_animals += 1

        # Eliminem l'element del mapa
        elements[x][y] = "·"
    return elements


def perdre_vida(elements):
    x, y = var_globals.jugador_x, var_globals.jugador_y
    simbol = elements[x][y]

    # Clau = nivell, valor = diccionari (clau = element, valor = vida que perd)   
    danys = {
        1: {"T": 20, "C": 30},
        2: {"T": 25, "C": 40},
        3: {"T": 30, "C": 50}
    }
    
    if simbol in danys[var_globals.level]:
        var_globals.jugador_vida -= danys[var_globals.level][simbol]
        elements[x][y] = '·'
    
    return elements


def main():
    return main()


if __name__ == "__main__":
    main()