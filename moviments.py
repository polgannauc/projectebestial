# S'implementen les regles del moviment de l'explorador

import var_globals


# Funcíó per desplaçar l'explorador en el mapa
def desplaçament(elements):
    entrada = input("cap on vols anar?(w, a, s ,d) ")
    nou_x, nou_y = var_globals.jugador_x, var_globals.jugador_y
    match entrada:
        case "w":
            # Calular el mòdul de la posició del jugador amb la mida del mapa resulta amb esfericitat en el mapa
            nou_x = (var_globals.jugador_x-1) % var_globals.mida 
        case "s":
            nou_x = (var_globals.jugador_x+1) % var_globals.mida
        case "a":
            nou_y = (var_globals.jugador_y-1) % var_globals.mida
        case "d":
            nou_y = (var_globals.jugador_y+1) % var_globals.mida
        case "q":
            var_globals.gameplay = False
            print("Sortint del joc...\nGràcies per jugar!!\n")
        case _:
            pass
    if elements[nou_x][nou_y] == "B":
        print("No pots creuar un bosc")
    else:
        var_globals.jugador_x, var_globals.jugador_y = nou_x, nou_y
    return elements