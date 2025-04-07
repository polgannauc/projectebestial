import var_globals
import mapa
import time

def main():
    dificultat = None
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

    var_globals.level = dificultat
    match dificultat:
        case 1:
            print("\nHas escollit el nivell 1: Piece of cake!")
            var_globals.mida = 5
            var_globals.entitats = {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1}
            var_globals.jugador_vida = 100
            var_globals.max_animals = 2
        case 2:
            print("\nHas escollit el nivell 2: Let's rock!")
            var_globals.mida = 10
            var_globals.entitats = {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3}
            var_globals.jugador_vida = 50
            var_globals.max_animals = 10
        case 3:
            print("\nHas escollit el nivell 3: Come get some!")
            var_globals.mida = 15
            var_globals.entitats = {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5}
            var_globals.jugador_vida = 25
            var_globals.max_animals = 18
    print("Carregant...")
    time.sleep(1.5)
    print("\n" * 30)
    mapa.main()


if __name__ == "__main__":
    main()
