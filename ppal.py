import var_globals
import mapa
import time
import sys

def set_level(nivell):
    var_globals.level
    var_globals.level = nivell

def get_level():
    return var_globals.level

def main():
    dificultat = get_level()
    seguir = False

    while not seguir:
        try:
            while dificultat not in [1, 2, 3]:
                print("Benvingut/uda al nostre joc")
                print("\nQuin nivell vols triar?")
                print("\n\tNivell 1: Piece of cake!")
                print("\n\tNivell 2: Let's rock!")
                print("\n\tNivell 3: Come get some!")
                dificultat = int(input("\nEscull nivell: "))
                seguir = False
            if dificultat in [1, 2, 3]:
                seguir = True
        except(ValueError):
            seguir = False

    set_level(dificultat)
    match dificultat:
        case 1:
            print("\nHas escollit el nivell 1: Piece of cake!")
        case 2:
            print("\nHas escollit el nivell 2: Let's rock!")
        case 3:
            print("\nHas escollit el nivell 3: Come get some!")
    print("Carregant...")
    time.sleep(1.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    mapa.main()


if __name__ == "__main__":
    main()
