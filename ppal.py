import random
import var_globals
import mapa

gameplay = False
level = 0

def set_level(nivell):
    global level
    level = nivell

def get_level():
    return level

def main():
    print("Benvingut/uda al nostre joc")
    print("\nQuin nivell vols triar?")
    print("\n\tNivell 1: Piece of cake!")
    print("\n\tNivell 2: Let's rock!")
    print("\n\tNivell 3: Come get some!")
    nivell = get_level()
    while nivell not in [1,2,3]:
        nivell = int(input("Escull nivell: "))
    set_level(nivell)
    match nivell:
        case 1:
            print("\nHas escollit el nivell 1: Piece of cake!")
            mapa.main()
        case 2:
            print("\nHas escollit el nivell 2: Let's rock!")
            mapa.main()
        case 3:
            print("\nHas escollit el nivell 3: Come get some!")
            mapa.main()
    
    #amplada_mapa = var_globals.mida_mapa(nivell)
    #print(amplada_mapa)
    #mapa.imprimir_mapa(amplada_mapa,amplada_mapa)
    


if __name__ == "__main__":
    main()