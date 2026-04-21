import random

# grafo
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 1), ('F', 6)],
    'D': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

# calcular costo de un camino
def costo_camino(camino):
    total = 0
    for i in range(len(camino)-1):
        for vecino, costo in grafo[camino[i]]:
            if vecino == camino[i+1]:
                total += costo
    return total

# generar vecinos (cambiar un tramo del camino)
def generar_vecinos(camino):
    vecinos = []

    for i in range(1, len(camino)-1):
        nodo = camino[i-1]

        for vecino, _ in grafo[nodo]:
            if vecino != camino[i]:
                nuevo = camino[:i] + [vecino]
                
                # completar camino aleatoriamente hasta G
                actual = vecino
                while actual != 'G':
                    if grafo[actual]:
                        actual = random.choice(grafo[actual])[0]
                        nuevo.append(actual)
                    else:
                        break

                if nuevo[-1] == 'G':
                    vecinos.append(nuevo)

    return vecinos


def tabu_search(inicio, objetivo, iteraciones=10, tamaño_tabu=3):
    # solución inicial simple
    actual = ['A', 'B', 'D', 'G']
    mejor = actual

    lista_tabu = []

    for i in range(iteraciones):
        print(f"\nIteración {i}")
        print("Actual:", actual, "Costo:", costo_camino(actual))

        vecinos = generar_vecinos(actual)

        mejor_vecino = None
        mejor_costo = float('inf')

        for v in vecinos:
            if v not in lista_tabu:
                c = costo_camino(v)
                if c < mejor_costo:
                    mejor_costo = c
                    mejor_vecino = v

        if mejor_vecino is None:
            break

        actual = mejor_vecino

        if costo_camino(actual) < costo_camino(mejor):
            mejor = actual

        lista_tabu.append(actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

        print("Mejor vecino:", actual, "Costo:", costo_camino(actual))
        print("Lista tabú:", lista_tabu)

    return mejor


# ejecutar
resultado = tabu_search('A', 'G')
print("\nMejor camino encontrado:", resultado)
print("Costo:", costo_camino(resultado))