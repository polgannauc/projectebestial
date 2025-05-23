# Mòdul on aniran les variables globals

def escollir_parametres(nivell):
    parametres_inicials = { # S'escullen els paràmetres inicilas segons el nivell de dificultat fent servir un diccionari
        1 : {"mida" : 5, "vida" : 100, "max_animals" : 2, "entitats" : {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1}, "missatge": "\nHas escollit el nivell 1: Piece of cake!"},
        2 : {"mida" : 10, "vida" : 50, "max_animals" : 10, "entitats" : {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3, "F": 1}, "missatge": "\nHas escollit el nivell 2: Let's rock!"},
        3 : {"mida" : 15, "vida" : 25, "max_animals" : 18, "entitats" : {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5, "F": 2}, "missatge": "\nHas escollit el nivell 3: Come get some!"}
    }
    return parametres_inicials.get(nivell)

def guardar_partida(ll_dades):
    with open('partida.txt', 'w') as f:
        for valor in ll_dades:
            f.write(str(valor) + "\n")

def carregar_partida():
    with open("partida.txt", "r") as f:
        ll_dades = f.readlines()
    return ll_dades

level = 0

gameplay = True # Variable de seguir el joc

guardar = False # Variable per guardar la partida

# Paràmetres inicials segons el nivell
mida = 0
entitats = {}
max_animals = 0
jugador_vida = 0

# Diccionari amb les direccions segons la mida del mapa, per calcular el camp de visió
dicc_direccions = {
    5: [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1), (-2, 0), (2, 0), (0, 2), (0, -2)],
    10: [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)],
    15: [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

# Posició del jugador
jugador_x = 0
jugador_y = 0

caselles_destapades = set() # Conjunt de les caselles que l'explorador ja ha visitat

comptador_animals = 0

visio_completa = 0 # Implementem una variable nova per controlar la visió de tot el mapa

activacio_inventari = False

inventari = {"ampolla" : 3, "ganivet" : 2}