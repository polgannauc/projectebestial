# Mòdul per imprimir el mapa
import var_globals
import elements
import moviments


def generar_visio(mida,pos_x,pos_y): # Posicions del jugador
    
    dicc_direccions = {
        5: [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)],
        10: [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)],
        15: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }
    camp_visio = []

    if var_globals.visio_completa > 0:
        # El camp de visió serà de tot el mapa
        camp_visio = [(x, y) for x in range(mida) for y in range(mida)]
    else:
        direccions = dicc_direccions[mida]
        for dx, dy in direccions: # Iterem en la llista de direccions, on es guarda la direcció x i direcció y 
            nou_dx = (pos_x+dx) % mida # La nova posició es calcula amb el mòdul per generar visió esfèrica
            nou_dy = (pos_y+dy) % mida
            camp_visio.append((nou_dx,nou_dy))
    return camp_visio


# Mapa que imprimeix els elements comparant-los amb un mapa destapat (matriu amb les lletres)
def mapa_tapat(mida, mapa_destapat,camp_visio, x, y):
    
    # Només s'actualitza el camp de visió si no hi ha visió completa
    if var_globals.visio_completa == 0:
        var_globals.caselles_destapades.update(camp_visio)

    # En cas d'haver visió completa, les caselles a mostrar son tot el camp de visió
    if var_globals.visio_completa > 0:
        caselles_a_mostrar = camp_visio
    # Si no hi ha visió completa, només es mostresn les caselles destapades que es van guardant en var_globals
    else:
        caselles_a_mostrar = var_globals.caselles_destapades

    for i in range(mida):
        print("+---" *mida+ "+")
        for j in range(mida):
            if (i,j)==(x,y):
                simbol ="E" # Si coinxideix amb la posició de l'explorador, l'imprimeix
            elif (i,j) in caselles_a_mostrar:
                # Evitem que imprimeixi a l'explorador sempre a la casella de sortida
                simbol = "." if mapa_destapat[i][j] == "E" else mapa_destapat[i][j]
            else:
                simbol ="X"
            print(f"| {simbol} ", end ="")
        print("|")
    print("+---" *mida+ "+")
    print(f"La teva salut és de: {var_globals.jugador_vida} punts de vida.\n")
    print(f"Has fotografiat {var_globals.comptador_animals} animals, te'n falten {var_globals.max_animals - var_globals.comptador_animals}.\n")


def main():
    elements_destapats = elements.generar_posicions(var_globals.mida, var_globals.entitats)

    while var_globals.gameplay:

        camp_visio = generar_visio(var_globals.mida, var_globals.jugador_x, var_globals.jugador_y)
        mapa_tapat(var_globals.mida, elements_destapats, camp_visio, var_globals.jugador_x, var_globals.jugador_y)

        if var_globals.jugador_vida<=0: # Condició derrota
            var_globals.gameplay= False
            print("Has perdut")
        elif var_globals.comptador_animals == var_globals.max_animals: # Condició victòria
            var_globals.gameplay = False 
            print("Has guanyat!")
        else:
            elements_destapats = moviments.desplaçament_jugador(elements_destapats)
        
        elements_destapats = elements.modificar_vida(elements_destapats)
        elements_destapats = elements.tocar_fada(elements_destapats)

        if var_globals.visio_completa > 0: # En cas d'activar-se la fada, en cada torn es va descontant el comptador de visió completa
            var_globals.visio_completa -= 1


if __name__ == "__main__":
    main()
