# Mòdul per establir el desplaçament del jugador
import var_globals


def desplaçament_jugador(elements):
    entrada = input("Cap on vols anar? (w, a, s, d, i per inventari, q per sortir): ")
    nou_x, nou_y = var_globals.jugador_x, var_globals.jugador_y
    match entrada:
        case "w":
            # Calular el mòdul de la posició del jugador amb la mida del mapa resulta en un map esfèric
            nou_x = (var_globals.jugador_x-1) % var_globals.mida 
        case "s":
            nou_x = (var_globals.jugador_x+1) % var_globals.mida
        case "a":
            nou_y = (var_globals.jugador_y-1) % var_globals.mida
        case "d":
            nou_y = (var_globals.jugador_y+1) % var_globals.mida
        case "q":
            var_globals.gameplay = False
            print("Gràcies per jugar!!")
        case "i":
            var_globals.activacio_inventari = True
        case _:
            pass
    if elements[nou_x][nou_y] == "B":  # Si és un bosc, el moviment no s'actualitza
        print("\nNo pots creuar un bosc")
    else: # Nómes s'apliquen els canvis del moviment si la casella no és un bosc
        var_globals.jugador_x, var_globals.jugador_y = nou_x, nou_y  
    return elements