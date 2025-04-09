import var_globals
import mapa
import time

def main():
    seguir = False
    print("Benvingut/uda al nostre joc")
    while not seguir:
        print("\nQuin nivell vols triar?")
        print("\n\tNivell 1: Piece of cake!")
        print("\n\tNivell 2: Let's rock!")
        print("\n\tNivell 3: Come get some!")
        entrada = input("\nEscull nivell: ")

        try:
            dificultat = int(entrada)

            if dificultat in [1, 2, 3]:
                seguir = True
            else:
                print("\nError: Només són vàlids els nivells 1, 2 i 3.")
        except ValueError:
            if entrada:
                print("\nError: Has d'introduir un número enter.")
            else:
                print("\nError: No has introduït res.")

    var_globals.level = dificultat

    parametres_inicials = { # S'escullen els paràmetres inicilas segons el nivell de dificultat fent servir un diccionari
        1 : {"mida" : 5, "vida" : 100, "max_animals" : 2, "entitats" : {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1}, "missatge": "\nHas escollit el nivell 1: Piece of cake!"},
        2 : {"mida" : 10, "vida" : 50, "max_animals" : 10, "entitats" : {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3}, "missatge": "\nHas escollit el nivell 2: Let's rock!"},
        3 : {"mida" : 15, "vida" : 25, "max_animals" : 18, "entitats" : {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5}, "missatge": "\nHas escollit el nivell 3: Come get some!"}
    }

    var_globals.mida = parametres_inicials[dificultat]["mida"]
    var_globals.jugador_vida = parametres_inicials[dificultat]["vida"]
    var_globals.max_animals = parametres_inicials[dificultat]["max_animals"]
    var_globals.entitats = parametres_inicials[dificultat]["entitats"]

    print(parametres_inicials[dificultat]["missatge"])

    print("Carregant...")
    time.sleep(1.5)
    print("\n" * 30)
    mapa.main()


if __name__ == "__main__":
    main()