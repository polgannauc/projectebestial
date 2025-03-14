# Aquest serà el mòdul pel mapa
import var_globals
import elements
import moviments

def mapa_parametres(var_nivell):
    match var_nivell:
        case 1:
            var_globals.mida = 5
            var_globals.entitats = {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1}
            var_globals.jugador_vida = 100
        case 2:
            var_globals.mida = 10
            var_globals.entitats = {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3}
            var_globals.jugador_vida = 50
        case 3:
            var_globals.mida = 15
            var_globals.entitats = {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5}
            var_globals.jugador_vida = 25
    return var_globals.mida, var_globals.entitats, var_globals.jugador_vida


# Funció per generar la visibilitat segons el nivell de dificultat
# Genera una llista amb les coordenades que pot veure l'explorador
# Paràmetres: mida que fa el mapa i les coordenades del jugador
def generar_visio(mida,x,y):
    ll_tuples = []
    direccions = []
    match mida:
        case 5:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)]
        case 10:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        case 15:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    for dx, dy in direccions:
        nou_dx = (x+dx) % mida
        nou_dy = (y+dy) % mida
        ll_tuples.append((nou_dx,nou_dy))
    return ll_tuples


def imprimir_mapa(mida,diccionari,visio,x,y):
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if i == x and j == y:
                print("| E ", end = "")
            else:
                key = False
                if (i,j) in visio:
                    for clau, valors in diccionari.items():
                        for valor in valors:
                            if (i, j) == valor:    
                                print(f"| {clau} ", end = "")
                                key = True
                    if key == False:
                        print(f"| · ", end = "")
                else:
                    print(f"| X ", end = "")
        print("|")
                           
                               
    print("+---" *mida+ "+")
    print(f"La teva salut és de: {var_globals.jugador_vida} punts de vida.\n")


# Faré un altre mapa per provar i no canviar l'anterior
def mapa_destapat(mida, mapa_destapat,visio, x, y):
    for fila in mapa_destapat:
        print(*fila)



def main():
    ll_elements = var_globals.ll_elements
    mapa_parametres(var_globals.level)
    # dic_posicions = elements.generar_posicions(var_globals.mida, ll_elements, var_globals.entitats)
    dic_posicions, elements_destapats = elements.generar_posicions(var_globals.mida, ll_elements, var_globals.entitats)
    
    while var_globals.gameplay:
        camp_visio = generar_visio(var_globals.mida,var_globals.jugador_x,var_globals.jugador_y)
        # imprimir_mapa(var_globals.mida,dic_posicions, camp_visio, var_globals.jugador_x, var_globals.jugador_y)
        mapa_destapat(var_globals.mida,elements_destapats,camp_visio,var_globals.jugador_x, var_globals.jugador_y)
        moviments.desplaçament()

if __name__ == "__main__":
    main()