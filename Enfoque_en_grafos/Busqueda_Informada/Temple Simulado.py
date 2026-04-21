import random
import math

# grafo
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 1), ('F', 6)],
    'D': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

# generar un camino aleatorio de A a G
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

# costo del camino
def costo(camino):
    total = 0
    for i in range(len(camino)-1):
        for vecino, c in grafo[camino[i]]:
            if vecino == camino[i+1]:
                total += c
    return total

# generar vecino (modificar camino)
def vecino(camino):
    if len(camino) <= 2:
        return camino_aleatorio()

    i = random.randint(1, len(camino)-2)
    nuevo = camino[:i]

    actual = camino[i-1]
    while actual != 'G':
        if grafo[actual]:
            actual = random.choice(grafo[actual])[0]
            nuevo.append(actual)
        else:
            break

    return nuevo

def temple_simulado(iteraciones=50, T_inicial=10, enfriamiento=0.95):
    actual = camino_aleatorio()
    mejor = actual

    T = T_inicial

    for i in range(iteraciones):
        nuevo = vecino(actual)

        delta = costo(nuevo) - costo(actual)

        if delta < 0:
            actual = nuevo
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                actual = nuevo

        if costo(actual) < costo(mejor):
            mejor = actual

        print(f"Iter {i} | T={T:.2f} | actual={actual} costo={costo(actual)}")

        T *= enfriamiento

    return mejor


# ejecutar
mejor = temple_simulado()
print("\nMejor camino encontrado:", mejor)
print("Costo:", costo(mejor))