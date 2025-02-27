# S'implementen les regles del moviment de l'explorador

import keyboard
import time
import ppal


def desplaçament(mida,x,y):
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
        ppal.gameplay = False
        print("Sortint del joc...")
    return x,y