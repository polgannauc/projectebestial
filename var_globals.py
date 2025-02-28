# En aquest mòdul és on aniran les variables globals
## Exemple: amplada del mapa o energia inicial
## Altres variables que podem posar, com les posicions de l'explorador i dels element
import random

gameplay = False
level = 0
jugador_x = 2
jugador_y = 2
#animal_x = 1
#animal_y = 1
jugador_vida = 0
entitats = {}
mida = 0


# Funció per generar la visibilitat segons el nivell de dificultat
# Funció per generar la visibilitat segons el nivell de dificultat
# Genera una llista amb les coordenades que pot veure l'explorador
# Paràmetres: mida que fa el mapa i les coordenades del jugador
def generar_visio(mida, pos_jugador):
    ll_tuples = []
    direccions = []
    match mida:
        case 5:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)]
        case 10:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        case 15:
            direccions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    x, y = pos_jugador[0], pos_jugador[1]
    for dx, dy in direccions:
        nou_dx = (x + dx) % mida
        nou_dy = (y + dy) % mida
        ll_tuples.append((nou_dx, nou_dy))
    return(ll_tuples)


#Llista amb tots els elements
ll_elements = ["E","A","T","R","L","B","C"] 