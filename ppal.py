import var_globals
import mapa
import time
import os

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
                print("\n" * 15 + "Error: Només són vàlids els nivells 1, 2 i 3.")
        except ValueError:
            if entrada:
                print("\n" * 15 + "Error: Has d'introduir un número enter.")
            else:
                print("\n" * 15 + "Error: No has introduït res.")

    var_globals.level = dificultat

    parametres = var_globals.escollir_parametres(dificultat)
    var_globals.mida = parametres["mida"]
    var_globals.jugador_vida = parametres["vida"]
    var_globals.max_animals = parametres["max_animals"]
    var_globals.entitats = parametres["entitats"]

    print(parametres["missatge"])

    print("Carregant...")
    time.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear") # Netejar la terminal. NT és de windows i fa cls. Si es linux, fa clear
    mapa.main()
 


if __name__ == "__main__":
    main()