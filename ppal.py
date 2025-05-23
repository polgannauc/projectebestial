import var_globals
import mapa
import elements
import moviments
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
        print("\n\tCarregar partida guardada (4).")
        entrada = input("\nEscull nivell: ")

        try:
            dificultat = int(entrada)
            if dificultat in [1, 2, 3, 4]:
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

    elements_destapats = elements.generar_posicions(var_globals.mida, var_globals.entitats)

    while var_globals.gameplay:

        camp_visio = mapa.generar_visio(var_globals.mida, var_globals.jugador_x, var_globals.jugador_y)
        mapa.mapa_tapat(var_globals.mida, elements_destapats, camp_visio, var_globals.jugador_x, var_globals.jugador_y)

        if var_globals.jugador_vida<=0: # Condició derrota
            var_globals.gameplay= False
            print("Has perdut")
        elif var_globals.comptador_animals == var_globals.max_animals: # Condició victòria
            var_globals.gameplay = False 
            print("Has guanyat!")
        else:
            elements_destapats = moviments.desplaçament_jugador(elements_destapats)
            elements_destapats = elements.modificar_vida(elements_destapats, var_globals.inventari)
            elements_destapats = elements.tocar_fada(elements_destapats)
        
            if var_globals.activacio_inventari: # Entra si s'activa l'inventari
                seguir = False
                while not seguir:
                    elements.mostrar_inventari(var_globals.inventari)
                    entrada = input("\nQuin objecte vols fer servir: ")
                    try:
                        eleccio = int(entrada)
                        if eleccio in [1, 2, 3]:
                            seguir = True
                        else:
                            print("\n" * 15 + "Error: Només es pot escollir l'ampolla o el ganivet")
                    except ValueError:
                        if entrada:
                            print("\n" * 15 + "Error: Has d'introduir un número per seleccionar l'objecte.")
                        else:
                            print("\n" * 15 + "Error: No has introduït res.")
                elements.utilitzar_objecte(eleccio, var_globals.inventari)
                var_globals.activacio_inventari = False

        if var_globals.visio_completa > 0: # En cas d'activar-se la fada, en cada torn es va descontant el comptador de visió completa
            var_globals.visio_completa -= 1

        # if var_globals.guardar == True:
        #     guardar_partida(var_globals.level ,var_globals.jugador_x, var_globals.jugador_y, elements_destapats, var_globals.inventari)
        #     var_globals.gameplay = False
 
if __name__ == "__main__":
    main()