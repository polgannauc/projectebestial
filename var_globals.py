import random



def mapa_base(fila, columna, element = None):
    mitja_f = int(fila / 2)
    mitja_c = int(columna / 2)
    columna += 1
    for i in range(fila):
        print("+---" * (columna - 1) + "+")
        for j in range(columna):
            caracter = element[random.randint(0, len(element) - 1)]
            if j == columna - 1:
                print("|")
            elif i == mitja_f and j == mitja_c:
                print(f"| E ", end = "")
            else:
                print(f"| {caracter}", end = "")
    print("+---" * (columna - 1) + "+")





def main():
    elements = ["X ", ". ", "A "]
    mapa_base(5, 5, elements)


if __name__ == "__main__":
    main()