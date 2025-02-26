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
animal = {'vida' : 10, 'exp' : 5}
jugador = {'hp' : 100, 'xp' : 0}


def foto():
    jugador['hp'] += animal['vida']
    jugador['xp'] += animal['exp']



def pos_elements(var_nivell):
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
    foto()

if __name__ == "__main__":
    main()