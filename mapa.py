# Mòdul per imprimir el mapa
import var_globals
import elements
import moviments


def generar_visio(mida,pos_x,pos_y): # Posicions del jugador
    match mida: # Segon la dificultat, genera un camps de visió més petit, o més gran
        case 5:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)]
        case 10:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        case 15:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    camp_visio = []
    for dx, dy in direccions: # Iterem en la llista de direccions, on es guarda la direcció x i direcció y 
        nou_dx = (pos_x+dx) % mida # La nova posició es calcula amb el mòdul per generar visió esfèrica
        nou_dy = (pos_y+dy) % mida
        camp_visio.append((nou_dx,nou_dy))
    return camp_visio


# Mapa que imprimeix els elements comparant-los amb un mapa destapat (matriu amb les lletres)
def mapa_tapat(mida, mapa_destapat,camp_visio, x, y):
    var_globals.caselles_destapades += list(set(camp_visio)) # Llista amb les posicions que ja ha vist l'explorador
    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if (i,j)==(x,y):
                print(f"| E ", end ="") # Si coinxideix amb la posició de l'explorador, l'imprimeix
            elif (i,j) in var_globals.caselles_destapades: 
                print(f"| {'·' if mapa_destapat[i][j] == 'E' else mapa_destapat[i][j]} ", end = "") # Posa un punt en la posició inicial de l'explorador, si és una altra posició, imprimeix l'element que pertoca
            else:
                print("| X ", end ="")
        print("|")
    print("+---" *mida+ "+")
    print(f"La teva salut és de: {var_globals.jugador_vida} punts de vida.\n")
    print(f"Has fotografiat {var_globals.comptador_animals} animals, te'n falten {var_globals.max_animals - var_globals.comptador_animals}.\n")



def main():
    elements_destapats = elements.generar_posicions(var_globals.mida, var_globals.entitats)

    while var_globals.gameplay:
        camp_visio = generar_visio(var_globals.mida,var_globals.jugador_x,var_globals.jugador_y)
        mapa_tapat(var_globals.mida,elements_destapats,camp_visio,var_globals.jugador_x, var_globals.jugador_y)

        elements_destapats = moviments.desplaçament_jugador(elements_destapats)
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