import var_globals
# On es troben definits tots el elements

## Llista d'elements:
### Casella oculat (X)
### Casella destapada (.)
### Animals (A)
### Trampes (T)
### Llac (L)
### Bosc (B)
### Refugi (R)
### Caçador (C)

#L’objectiu del joc és trobar-los i fotografiar-los.
# Suma punts d’energia per cada animal fotografiat (segons el nivell) i es guarda a la llista d’animals fotografiats.
# Un cop la casella ha estat visitada s’ha de mostrar el símbol de la casella destapada.

jugador = {'hp' : 100, 'xp' : 0}
animal = {'hp' : 10, 'xp' : 5}
#x_animal = 1
#y_animal = 1

# Funció per generar un diccionari que conté com a clau la A (d'animal) i com a valor una llista de tuples
# amb les posicions generades a l'atzar.
# S'ha de tenir en compte l'amplada del mapa, i més endvant, si fem un diccionari per cada element o un amb tots
# També tenir en compte que no es poden solapar les posicions dels elements. 
def pos_elements(var_nivell):
    global x_animal
    global y_animal
    dicc_elements = {} 
    match var_nivell:
        case 1:
            q_animals = 2
            llista_animals = []
            for i in range(q_animals):
                x_animal = var_globals.random.randint(0, var_globals.mida_mapa - 1)
                y_animal = var_globals.random.randint(0, var_globals.mida_mapa - 1)
                llista_animals.append((x_animal, y_animal))
    dicc_elements['A'] = llista_animals
    return dicc_elements

#animals = pos_elements(var_globals.ppal.get_level())
#print(animals)

if __name__ == "__main__":
        pos_elements(var_globals.ppal.get_level())