# Mòdul per imprimir el mapa
import var_globals
import elements
import moviments


# Funció per generar la visibilitat segons el nivell de dificultat
# Genera una llista amb les coordenades que pot veure l'explorador
# Paràmetres: mida que fa el mapa i les coordenades del jugador
def generar_visio(mida,x,y):
    match mida:
        case 5:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)]
        case 10:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        case 15:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    ll_tuples = []
    for dx, dy in direccions:
        nou_dx = (x+dx) % mida
        nou_dy = (y+dy) % mida
        ll_tuples.append((nou_dx,nou_dy))
    return ll_tuples



# Mapa que imprimeix els elements comparant-los amb un mapa destapat (matriu amb les lletres)
def mapa_tapat(mida, mapa_destapat,camp_visio, x, y):
    var_globals.caselles_destapades += list(set(camp_visio))
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if (i,j)==(x,y):
                print(f"| E ", end ="")
            elif (i,j) in var_globals.caselles_destapades:
                print(f"| {'·' if mapa_destapat[i][j] == 'E' else mapa_destapat[i][j]} ", end = "") # If i else en una mateixa línia 
            else:
                print("| X ", end ="")
        print("|")
    print("+---" *mida+ "+")
    print(f"La teva salut és de: {var_globals.jugador_vida} punts de vida.\n")



def main():
    elements_destapats = elements.generar_posicions(var_globals.mida, var_globals.entitats)
    while var_globals.gameplay:
        camp_visio = generar_visio(var_globals.mida,var_globals.jugador_x,var_globals.jugador_y)
        mapa_tapat(var_globals.mida,elements_destapats,camp_visio,var_globals.jugador_x, var_globals.jugador_y)

        elements_destapats = moviments.desplaçament(elements_destapats)
        elements_destapats = elements.guanyar_vida(elements_destapats)
        elements_destapats = elements.perdre_vida(elements_destapats)

        if var_globals.jugador_vida<=0:
            var_globals.gameplay= False
            print("Has perdut")
        if var_globals.comptador_animals == var_globals.max_animals:
            print("Has guanyat")
            var_globals.gameplay = False 

    
    

if __name__ == "__main__":
    main()