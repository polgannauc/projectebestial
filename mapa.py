# Generació del tauler (mapa) i la col·locació dels elements
# També gestionar les regles de cada element

import random
import elements
import keyboard

def imprimir_mapa(fila, columna, llista_elements):
    columna+=1
    for i in range(fila):
        print("+---" * (columna-1) + "+")
        for j in range(columna):
            caracter = llista_elements[random.randint(0,len(llista_elements)-1)]
            if j == columna-1:
                print("|")
            elif j==2 and i ==2:
                print(f"| E ", end ="")
            else:
                print(f"| {caracter}", end ="")
    print("+---" * (columna-1) + "+")


elements = ["X ", ". ","A "]
        
imprimir_mapa(5,5,elements)




def main():
    imprimir_mapa()


if __name__ == "__main__":
    main()