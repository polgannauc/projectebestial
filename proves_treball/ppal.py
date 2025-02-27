import random
import var_globals
import mapa

def main():
    print("Benvingut/uda al nostre joc")
    print("\nQuin nivell vols triar?")
    print("\n\tNivell 1: Piece of cake!")
    print("\n\tNivell 2: Let's rock!")
    print("\n\tNivell 3: Come get some!")
    level = None
    while level not in [1,2,3]:
        level = int(input("Escull nivell: "))
    match level:
        case 1:
            print("\nHas escollit el nivell 1: Piece of cake!")
        case 2:
            print("\nHas escollit el nivell 2: Let's rock!")
        case 3:
            print("\nHas escollit el nivell 3: Come get some!")
    
    amplada_mapa = var_globals.mida_mapa(level)
    print(amplada_mapa)
    #mapa.imprimir_mapa(amplada_mapa,amplada_mapa)
    



if __name__ == "__main__":
    main()