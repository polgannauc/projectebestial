#L’objectiu del joc és trobar-los i fotografiar-los.
# Suma punts d’energia per cada animal fotografiat (segons el nivell) i es guarda a la llista d’animals fotografiats.
# Un cop la casella ha estat visitada s’ha de mostrar el símbol de la casella destapada.

animal = {'vida' : 10, 'exp' : 5}
jugador = {'hp' : 100, 'xp' : 0}


def foto():
    jugador['hp'] += animal['vida']
    jugador['xp'] += animal['exp']









def main():
    foto()

if __name__ == "__main__":
    main()