# Mòdul on aniran les variables globals

def escollir_parametres(nivell):
    parametres_inicials = { # S'escullen els paràmetres inicilas segons el nivell de dificultat fent servir un diccionari
        1 : {"mida" : 5, "vida" : 100, "max_animals" : 2, "entitats" : {"E": 1, "A": 2, "T": 2, "R": 2, "L": 4, "B": 2, "C": 1}, "missatge": "\nHas escollit el nivell 1: Piece of cake!"},
        2 : {"mida" : 10, "vida" : 50, "max_animals" : 10, "entitats" : {"E": 1, "A": 10, "T": 10, "R": 6, "L": 14, "B": 10, "C": 3, "F": 1}, "missatge": "\nHas escollit el nivell 2: Let's rock!"},
        3 : {"mida" : 15, "vida" : 25, "max_animals" : 18, "entitats" : {"E": 1, "A": 18, "T": 25, "R": 16, "L": 20, "B": 25, "C": 5, "F": 2}, "missatge": "\nHas escollit el nivell 3: Come get some!"}
    }
    return parametres_inicials.get(nivell)

level = 0

guardar = False

gameplay = True # Variable de seguir el joc

# Paràmetres inicials segons el nivell
mida = 0
entitats = {}
max_animals = 0
jugador_vida = 0

# Posició del jugador
jugador_x = 0
jugador_y = 0

caselles_destapades = set() # Conjunt de les caselles que l'explorador ja ha visitat

comptador_animals = 0

visio_completa = 0 # Implementem una variable nova per controlar la visió de tot el mapa


activacio_inventari = False

inventari = {"ampolla" : 3, "ganivet" : 2}