# Mòdul per imprimir el mapa
import var_globals

def generar_visio(mida,pos_x,pos_y): # Posicions del jugador
    camp_visio = []
    for dx, dy in var_globals.dicc_direccions[mida]: # Iterem en la llista de direccions, on es guarda la direcció x i direcció y
        nou_dx = (pos_x+dx) % mida # La nova posició es calcula amb el mòdul per generar visió esfèrica
        nou_dy = (pos_y+dy) % mida
        camp_visio.append((nou_dx,nou_dy))
    return camp_visio


# Mapa que imprimeix els elements comparant-los amb un mapa destapat (matriu amb les lletres)
def mapa_tapat(mida, mapa_destapat,camp_visio, x, y):
    # S'actualitza el camp de visió si no hi ha visió completa
    var_globals.caselles_destapades.update(camp_visio)

    # Si hi ha visió completa, es mostra tot el mapa. Sino, es mostren les caselles destapades
    caselles_a_mostrar = ([(x, y) for x in range(mida) for y in range(mida)] if var_globals.visio_completa > 0 else var_globals.caselles_destapades)
    
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