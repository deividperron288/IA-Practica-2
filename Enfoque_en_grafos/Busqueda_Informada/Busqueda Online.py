import random

# Grafo "real" (el agente NO lo conoce completo)
grafo_real = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['C', 'F'],
    'F': ['E', 'G'],
    'G': []
}

# memoria del agente
visitados = set()
padres = {}

def obtener_vecinos(nodo):
    # el agente solo ve vecinos al llegar
    return grafo_real[nodo]

def busqueda_online(inicio, objetivo):
    actual = inicio
    padres[actual] = None

    while actual != objetivo:
        print("Estoy en:", actual)

        visitados.add(actual)

        vecinos = obtener_vecinos(actual)

        # elegir vecino no visitado
        siguiente = None
        for v in vecinos:
            if v not in visitados:
                siguiente = v
                break

        # si todos visitados → retroceder
        if siguiente is None:
            print("Retrocediendo...")
            actual = padres[actual]
            continue

        padres[siguiente] = actual
        actual = siguiente

    print("Llegué a:", objetivo)

    # reconstruir camino
    camino = []
    nodo = objetivo
    while nodo:
        camino.append(nodo)
        nodo = padres[nodo]

    return camino[::-1]


# ejecutar
camino = busqueda_online('A', 'G')
print("\nCamino encontrado:", camino)