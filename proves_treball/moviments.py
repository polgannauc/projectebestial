# S'implementen les regles del moviment de l'explorador

import keyboard
import time


def desplaçament(mida,x,y):
    global gameplay
    if keyboard.is_pressed("w"):
        x -= 1
        if x== -1:
            x=mida-1
    elif keyboard.is_pressed("s"):
        x += 1
        if x== mida:
            x=0
    elif keyboard.is_pressed("a"):
        y -= 1
        if y==-1:
            y=mida-1
    elif keyboard.is_pressed("d"):
        y += 1
        if y==mida:
            y=0
    elif keyboard.is_pressed("q"):
        gameplay = False
    return x,y


# def imprimir_mapa(mida,x,y):
#     for i in range(mida):
#         print("+---" *mida+ "+")
#         for j in range(mida):
#             if j == mida - 1: 
#                 if i == x and j == y:
#                     print("| E ", end="")
#                 else:
#                     print("|   ", end="")
#                 print("|") 
#             else:
#                 if i == x and j == y:
#                     print("| E ", end="")
#                 else:
#                     print("|   ", end="")
#     print("+---" *mida+ "+")


# jugador_x = 2
# jugador_y = 2
# amplada_mapa = 5  
# gameplay = True

# imprimir_mapa(amplada_mapa,jugador_x,jugador_y)

# while gameplay:
#     old_x,old_y = jugador_x, jugador_y
#     jugador_x, jugador_y = desplaçament(amplada_mapa,jugador_x,jugador_y)

#     if jugador_x!=old_x or jugador_y!=old_y:
#         imprimir_mapa(amplada_mapa,jugador_x,jugador_y)
#         time.sleep(0.2)
    