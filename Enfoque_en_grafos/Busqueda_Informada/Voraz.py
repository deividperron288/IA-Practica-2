import heapq

grafo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 10)],
    'C': [('F', 2)],
    'D': [],
    'E': [],
    'F': [('G', 4)],
    'G': []
}

heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

def voraz(inicio, objetivo):
    cola = []
    
    # 🔹 guardamos (heurística, nodo)
    heapq.heappush(cola, (heuristica[inicio], inicio))
    
    visitados = set()
    padres = {inicio: None}
    costos = {inicio: 0}  # costo acumulado desde el inicio

    while cola:
        # 🔹 sacamos el nodo con menor h(n)
        _, nodo = heapq.heappop(cola)

        print("Visitando:", nodo)

        if nodo == objetivo:
            print("¡Encontrado!")
            costo_final = costos[objetivo]
            print(f"Costo del camino final: {costo_final}")
            break

        visitados.add(nodo)

        # 🔹 recorrer vecinos (como en tu ejemplo del for con comas)
        for vecino, costo in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(cola, (heuristica[vecino], vecino))
                padres[vecino] = nodo
                costos[vecino] = costos[nodo] + costo  # acumular costo

    # reconstruir camino
    camino = []
    nodo = objetivo
    while nodo: 
        camino.append(nodo)
        nodo = padres[nodo]

    return camino[::-1]

# Ejecutar
print("Camino:", voraz('A', 'G'))