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



# Mapa que imprimeix els elements comparant-los amb un mapa destapat (matriu amb les lletres)
def mapa_tapat(mida, mapa_destapat,visio, x, y):
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if (i,j)==(x,y):
                print(f"| E ", end ="")
            elif (i,j) in visio:
                print(f"| {"·" if mapa_destapat[i][j] == "E" else mapa_destapat[i][j]} ", end = "") # If i else en una mateixa línia 
            else:
                print("| X ", end ="")
        print("|")
    print("+---" *mida+ "+")
    print(f"La teva salut és de: {var_globals.jugador_vida} punts de vida.\n")



def main():
    mapa_parametres(var_globals.level)
    elements_destapats = elements.generar_posicions(var_globals.mida, var_globals.ll_elements, var_globals.entitats)
    while var_globals.gameplay:
        camp_visio = generar_visio(var_globals.mida,var_globals.jugador_x,var_globals.jugador_y)
        mapa_tapat(var_globals.mida,elements_destapats,camp_visio,var_globals.jugador_x, var_globals.jugador_y)
        elements_destapats= elements.animal(elements_destapats)
        moviments.desplaçament()

if __name__ == "__main__":
    main()