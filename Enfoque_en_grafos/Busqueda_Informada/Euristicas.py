import heapq

grafo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 10)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [],
    'F': [('G', 4)],
    'G': []
}

heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 6,
    'F': 2,
    'G': 0
}

def a_estrella(inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))
    
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        _, nodo = heapq.heappop(cola)
        print("Visitando:", nodo)

        if nodo == objetivo:
            break

        for vecino, costo in grafo[nodo]:
            nuevo_costo = costos[nodo] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino]
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = nodo

    # reconstruir camino
    camino = []
    nodo = objetivo
    while nodo:
        camino.append(nodo)
        nodo = padres[nodo]
    
    return camino[::-1]

# Ejecutar
print("Camino:", a_estrella('A', 'G'))