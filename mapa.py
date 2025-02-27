# Aquest serà el mòdul pel mapa
import var_globals
import time
import moviments
import ppal


def imprimir_mapa(mida,diccionari,x,y):
    ppal.gameplay = True
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if j == mida - 1: 
                if i == x and j == y:
                    print("| E ", end="")
                else:
                    print("|   ", end="")
                print("|") 
            else:
                if i == x and j == y:
                    print("| E ", end="")
                else:
                    print("|   ", end="")
    print("+---" *mida+ "+")



def main():
    ll_elements=var_globals.ll_elements
    amplada = var_globals.mida_mapa(1)
    dic_q_elements=var_globals.quantitat_elements(1)
    dic_posicions = var_globals.generar_posicions(amplada,ll_elements,dic_q_elements)

    jugador_x = 2
    jugador_y = 2

    imprimir_mapa(amplada,dic_posicions,jugador_x,jugador_y)

    while ppal.gameplay:
        old_x,old_y = jugador_x, jugador_y
        jugador_x, jugador_y = moviments.desplaçament(amplada,jugador_x,jugador_y)

        if jugador_x!=old_x or jugador_y!=old_y:
            imprimir_mapa(amplada,dic_posicions,jugador_x,jugador_y)
            time.sleep(0.2)

if __name__ == "__main__":
    main()