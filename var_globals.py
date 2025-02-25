def mapa_base(fila, columna, elements = None):
    mitja_f = fila / 2
    mitja_c = columna / 2
    columna += 1
    for i in range(fila):
        print("+---" * (columna - 1) + "+")
        for j in range(columna):
            if j == columna - 1:
                print("|")
            elif i == mitja_f and j == mitja_c:
                print(f"| E ", end = "")
            else:
                print(f"|   ", end = "")
    print("+---" * (columna - 1) + "+")





def main():
    mapa_base(5,5)


if __name__ == "__main__":
    main()