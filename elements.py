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



#Funció per generar un diccionari on cada clau és l'element i el valor la quantitat de vegades que apareix en el mapa segons dificultat
def quantitat_elements(var_nivell):
    nivells = { # Generem un diccionari, on cada nivell és la clau, i el valor un diccionari amb els elements i la quantitat
        1: {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1},
        2: {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3},
        3: {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5},
    }
    return nivells.get(var_nivell, {}) #Ens retornarà només un diccionari segons el nivell, o un diccionari buit


# Funció per generar la visibilitat segons el nivell de dificultat
# Generar un diccionari amb cada element com a clau (E,A,B) i els valors com llistes de tuples amb les posicions
# Accepta com a paràmetres: mida del mapa, llista amb els elements, diccionari amb quantitat de cada element segons el nivell
def generar_posicions(mida,ll_elements,diccionari):
    dic_pos = {}
    combinacions_possibles = [(x, y) for x in range(mida) for y in range(mida)]
    random.shuffle(combinacions_possibles)
    for i in ll_elements:
        ll_aux = []
        for j in range(diccionari[i]):
            ll_aux.append(combinacions_possibles.pop())
        dic_pos[i]=ll_aux
    return dic_pos



animal = {'hp' : 10, 'xp' : 5}
x_animal = 1
y_animal = 1
jugador = {'hp' : 100, 'xp' : 0}

# animals = pos_elements(1)
# print(animals)


# # def main():
# #     # pos_elements(1)

# if __name__ == "__main__":
#     main()