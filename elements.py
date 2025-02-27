# On es troben definits tots el elements

## Llista d'elements:
### Casella oculat (X)
### Casella destapada (.)
### Animals (A)
### Trampes (T)
### Llac (L)
### Bosc (B)
### Refugi (R)
### Caçador (C)

#L’objectiu del joc és trobar-los i fotografiar-los.
# Suma punts d’energia per cada animal fotografiat (segons el nivell) i es guarda a la llista d’animals fotografiats.
# Un cop la casella ha estat visitada s’ha de mostrar el símbol de la casella destapada.

import var_globals
import random

animal = {'hp' : 10, 'xp' : 5}
x_animal = 1
y_animal = 1
jugador = {'hp' : 100, 'xp' : 0}



# Funció per generar un diccionari que conté com a clau la A (d'animal) i com a valor una llista de tuples
# amb les posicions generades a l'atzar.
# S'ha de tenir en compte l'amplada del mapa, i més endvant, si fem un diccionari per cada element o un amb tots
# També tenir en compte que no es poden solapar les posicions dels elements. 
def pos_elements(var_nivell):
    global x_animal
    global y_animal
    dicc_elements = {} 
    match var_nivell:
        case 1:
            q_animals = 2
            ll = []
            for i in range(q_animals):
                x_animal= random.randint(0,var_globals.amplada_mapa-1)
                y_animal= random.randint(0,var_globals.amplada_mapa-1)
                ll.append((x_animal,y_animal))
    dicc_elements["A"]=ll
    return dicc_elements

animals = pos_elements(1)
print(animals)


def main():
    pos_elements(1)

if __name__ == "__main__":
    main()