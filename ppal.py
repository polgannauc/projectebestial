# En aquest part és on s'inicia el joc i mostra el resultat final
## Entenc que aquest mòdul és on es criden la resta de funcions dels altres mò


import keyboard
import mapa

gameplay = False

def demanar_opcio():
    global gameplay
    opcio = int(input("Benvingut al menú, quina dificultat vols agafar?\n1. Fàcil\n2. Mitjà\n3. Difícil\n"))
    match opcio:
        case 1:
            print(f"Has triat la opció: {opcio}. Fàcil: Piece of cake!")
            gameplay = True
            mapa.imprimir_mapa(5,5,mapa.elements)
            return opcio
        case 2:
            print(f"Has triat la opció: {opcio}. Mitjà: Let's rock!")
            gameplay = True
            mapa.imprimir_mapa(10,10,mapa.elements)
            return opcio
        case 3:
            print(f"Has triat la opció: {opcio}. Difícil: Come get some!")
            gameplay = True
            mapa.imprimir_mapa(15,15,mapa.elements)
            return opcio
        case _:
            return opcio


def main():
    while demanar_opcio() not in [1, 2, 3]:
        demanar_opcio()

if __name__ == "__main__":
    main()