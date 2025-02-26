# En aquest mòdul és on aniran les variables globals
## Exemple: amplada del mapa o energia inicial
## Altres variables que podem posar, com les posicions de l'explorador i dels elements

import random

# Funció per escollir la mida del mapa segons nivell de dificultat:
def mida_mapa(var_nivell):
    mida = None
    match var_nivell:
        case 1:
            mida = 5
        case 2:
            mida = 10
        case 3:
            mida = 15
    return mida

amplada_mapa = mida_mapa(1)

# Crec la posició on inicia el jugador hauria de ser a l'atzar
# Per tant, s'ha de generar de manera aleatoria segons la mida del mapa

x_jugador = random.randint(0,amplada_mapa-1)
y_jugador = random.randint(0,amplada_mapa-1)

print(f"La posició del jugador és la següent:({x_jugador},{y_jugador})")








# # Et deixo el mapa que estaves fent
# def mapa_base(fila, columna, element = None):
#     mitja_f = int(fila / 2)
#     mitja_c = int(columna / 2)
#     columna += 1
#     for i in range(fila):
#         print("+---" * (columna - 1) + "+")
#         for j in range(columna):
#             caracter = element[random.randint(0, len(element) - 1)]
#             if j == columna - 1:
#                 print("|")
#             elif i == mitja_f and j == mitja_c:
#                 print(f"| E ", end = "")
#             else:
#                 print(f"| {caracter}", end = "")
#     print("+---" * (columna - 1) + "+")





# def main():
#     elements = ["X ", ". ", "A "]
#     mapa_base(5, 5, elements)


# if __name__ == "__main__":
#     main()