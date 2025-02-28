# Aquest serà el mòdul pel mapa
import var_globals

jugador_x = 2
jugador_y = 2

def imprimir_mapa(mida,diccionari,x,y):
    matriu = []
    var_globals.ppal.gameplay = True
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



def main():
    global jugador_x
    global jugador_y
    ll_elements=var_globals.ll_elements
    amplada = var_globals.mida_mapa(1)
    dic_q_elements = var_globals.quantitat_elements(1)
    dic_posicions = var_globals.generar_posicions(amplada,ll_elements,dic_q_elements)

    imprimir_mapa(amplada,dic_posicions,jugador_x,jugador_y)

    print(f"La teva salut és de: {var_globals.elements.jugador['hp']}")

    while var_globals.ppal.gameplay:
        old_x,old_y = jugador_x, jugador_y
        jugador_x, jugador_y = var_globals.moviments.desplaçament(amplada,jugador_x,jugador_y)

        if jugador_x!=old_x or jugador_y!=old_y:
            imprimir_mapa(amplada,dic_posicions,jugador_x,jugador_y)
            var_globals.time.sleep(0.2)

        if jugador_x == var_globals.elements.x_animal and jugador_y == var_globals.elements.y_animal:
            var_globals.elements.jugador['xp'] += var_globals.elements.animal['xp']

if __name__ == "__main__":
    main()