import random

grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 1), ('F', 6)],
    'D': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

# costo de un camino
def costo(camino):
    total = 0
    for i in range(len(camino)-1):
        for vecino, c in grafo[camino[i]]:
            if vecino == camino[i+1]:
                total += c
    return total

# generar un camino aleatorio A → G
def camino_aleatorio():
    camino = ['A']
    actual = 'A'
    while actual != 'G':
        vecinos = grafo[actual]
        if not vecinos:
            break
        actual = random.choice(vecinos)[0]
        camino.append(actual)
    return camino

# generar vecinos de un camino
def vecinos(camino):
    lista = []
    for i in range(1, len(camino)-1):
        nodo = camino[i-1]
        for v, _ in grafo[nodo]:
            if v != camino[i]:
                nuevo = camino[:i] + [v]

                actual = v
                while actual != 'G':
                    if grafo[actual]:
                        actual = random.choice(grafo[actual])[0]
                        nuevo.append(actual)
                    else:
                        break

                if nuevo[-1] == 'G':
                    lista.append(nuevo)
    return lista

def haz_local(k=2, iteraciones=10):
    # estados iniciales
    estados = [camino_aleatorio() for _ in range(k)]

    for i in range(iteraciones):
        print(f"\nIteración {i}")
        for e in estados:
            print("Estado:", e, "Costo:", costo(e))

        todos_vecinos = []
        for e in estados:
            todos_vecinos.extend(vecinos(e))

        if not todos_vecinos:
            break

        # ordenar por costo (mejor primero)
        todos_vecinos.sort(key=costo)

        # quedarnos con los k mejores
        estados = todos_vecinos[:k]

    return estados[0]

# ejecutar
mejor = haz_local(k=2, iteraciones=10)
print("\nMejor camino encontrado:", mejor)
print("Costo:", costo(mejor))