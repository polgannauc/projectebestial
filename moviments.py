# S'implementen les regles del moviment de l'explorador

import var_globals


def desplaçament():
    entrada = input("cap on vols anar?(w, a, s ,d) ")
    match entrada:
        case "w":
            var_globals.jugador_x -= 1
            if var_globals.jugador_x == -1:
                var_globals.jugador_x = var_globals.mida - 1
        case "s":
            var_globals.jugador_x += 1
            if var_globals.jugador_x == var_globals.mida:
                var_globals.jugador_x = 0
        case "a":
            var_globals.jugador_y -= 1
            if var_globals.jugador_y == -1:
                var_globals.jugador_y = var_globals.mida - 1
        case "d":
            var_globals.jugador_y += 1
            if var_globals.jugador_y == var_globals.mida:
                var_globals.jugador_y = 0
        case "q":
            var_globals.gameplay = False
            print("Sortint del joc...\nGràcies per jugar!!\n")
        case _:
            var_globals.jugador_x == var_globals.jugador_x
            var_globals.jugador_y == var_globals.jugador_y
