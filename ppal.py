import var_globals
import mapa


def set_level(nivell):
    var_globals.level
    var_globals.level = nivell

def get_level():
    return var_globals.level

def main():
    print("Benvingut/uda al nostre joc")
    print("\nQuin nivell vols triar?")
    print("\n\tNivell 1: Piece of cake!")
    print("\n\tNivell 2: Let's rock!")
    print("\n\tNivell 3: Come get some!")

    dificultat = get_level()

    while dificultat not in [1,2,3]:
        dificultat = int(input("\nEscull nivell: "))

    set_level(dificultat)
    match dificultat:
        case 1:
            print("\nHas escollit el nivell 1: Piece of cake!")
        case 2:
            print("\nHas escollit el nivell 2: Let's rock!")
        case 3:
            print("\nHas escollit el nivell 3: Come get some!")
    mapa.main()


if __name__ == "__main__":
    main()