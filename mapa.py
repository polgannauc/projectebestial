# Aquest serà el mòdul pel mapa
import var_globals
import time
import elements
import moviments

def imprimir_mapa(mida,diccionari,x,y):
    matriu = []
    var_globals.gameplay = True
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if j == mida - 1: 
                if i == x and j == y:
                    print("| E ", end="")
                else:
                    print(f"| · ", end="")
                print("|") 
            else:
                if i == x and j == y:
                    print("| E ", end="")
                else:
                    print(f"| · ", end="")
    print("+---" *mida+ "+")
    
    print(f"La teva salut és de: {var_globals.jugador['hp']} punts de vida.")



def main():
    global jugador_x
    global jugador_y
    ll_elements = var_globals.ll_elements
    level = var_globals.level
    amplada = var_globals.mida_mapa(level)
    dic_q_elements = elements.quantitat_elements(level)
    dic_posicions = elements.generar_posicions(amplada,ll_elements,dic_q_elements)

    imprimir_mapa(amplada,dic_posicions,var_globals.jugador_x,var_globals.jugador_y)

    while var_globals.gameplay:
        old_x,old_y = var_globals.jugador_x, var_globals.jugador_y
        var_globals.jugador_x, var_globals.jugador_y = moviments.desplaçament(amplada,var_globals.jugador_x,var_globals.jugador_y)

        if var_globals.jugador_x != old_x or var_globals.jugador_y != old_y:
            imprimir_mapa(amplada,dic_posicions,var_globals.jugador_x,var_globals.jugador_y)
            time.sleep(0.2)

        #if jugador_x == elements.x_animal and jugador_y == elements.y_animal:
        #    elements.jugador['xp'] += elements.animal['xp']

if __name__ == "__main__":
    main()