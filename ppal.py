def demanar_opcio():
    opcio = int(input("Benvingut al menú, quina dificultat vols agafar?\n1. Fàcil\n2. Mitjà\n3. Difícil\n"))
    match opcio:
        case 1:
            print(f"Has triat la opció: {opcio}. Fàcil")
            return opcio
        case 2:
            print(f"Has triat la opció: {opcio}. Mitjà")
            return opcio
        case 3:
            print(f"Has triat la opció: {opcio}. Difícil")
            return opcio
        case _:
            return opcio


def main():
    while demanar_opcio() not in [1, 2, 3]:
        demanar_opcio()



if __name__ == "__main__":
    main()