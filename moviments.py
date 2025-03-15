# S'implementen les regles del moviment de l'explorador

import var_globals


# Funcíó per desplaçar l'explorador en el mapa
def desplaçament():
    entrada = input("cap on vols anar?(w, a, s ,d) ")
    match entrada:
        case "w":
            # Calular el mòdul de la posició del jugador amb la mida del mapa resulta amb esfericitat en el mapa
            var_globals.jugador_x = (var_globals.jugador_x-1) % var_globals.mida 
        case "s":
            var_globals.jugador_x = (var_globals.jugador_x+1) % var_globals.mida
        case "a":
            var_globals.jugador_y = (var_globals.jugador_y-1) % var_globals.mida
        case "d":
            var_globals.jugador_y = (var_globals.jugador_y+1) % var_globals.mida
        case "q":
            var_globals.gameplay = False
            print("Sortint del joc...\nGràcies per jugar!!\n")
        case _:
            pass