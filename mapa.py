# Generació del tauler (mapa) i la col·locació dels elements
# També gestionar les regles de cada element
import random
import elements
import keyboard
import var_globals

def imprimir_mapa(fila, columna, llista_elements):
    columna+=1
    for i in range(fila):
        print("+---" * (columna-1) + "+")
        for j in range(columna):
            if j == columna-1:
                print("|")
            else:
                if i == var_globals.x_jugador and j == var_globals.y_jugador:
                    print(f"| E ", end ="")
                else:
                    print(f"| {llista_elements[random.randint(0,len(llista_elements)-1)]} ", end ="")
    print("+---" * (columna-1) + "+")

# def mapa_ocult()  Funció per mostrar el mapa ocult i, a mesura que el jugador es mou, es va revelant el mapa
# La visió també anirà aqui??

elements = ["A","T","L","B","R","C"]

def main():
    imprimir_mapa(5,5,elements)


if __name__ == "__main__":
    main()