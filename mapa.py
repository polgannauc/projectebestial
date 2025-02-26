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
            if j == columna-1:
                print("|")
            else:
                if i == 0 and j == 0:
                    print(f"| E ", end ="")
                else:
                    print(f"| {llista_elements[random.randint(0,len(llista_elements)-1)]} ", end ="")
    print("+---" * (columna-1) + "+")


elements = ["A",]
        
imprimir_mapa(5,5,elements)



# def mapa_ocult()  Funció per mostrar el mapa ocult i, a mesura que el jugador es mou, es va revelant el mapa
# La visió també anirà aqui??


def main():
    imprimir_mapa()


if __name__ == "__main__":
    main()