import heapq

# A*
# =========================

grafo_a = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristica_a = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 5, 'E': 3, 'F': 1, 'G': 0
}

def a_estrella(inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))

    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        _, nodo = heapq.heappop(cola)
        print("[A*] Visitando:", nodo)

        if nodo == objetivo:
            break

        for vecino, costo in grafo_a[nodo]:
            nuevo = costos[nodo] + costo

            if vecino not in costos or nuevo < costos[vecino]:
                costos[vecino] = nuevo
                prioridad = nuevo + heuristica_a[vecino]
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = nodo

    # reconstruir camino
    camino = []
    n = objetivo
    while n:
        camino.append(n)
        n = padres[n]
    return camino[::-1], costos[objetivo]


# =========================
# AO*


grafo_ao = {
    'A': ('OR', ['B', 'C']),
    'B': ('AND', ['D', 'E']),
    'C': ('OR', ['F', 'G']),
    'D': ('OR', []),
    'E': ('OR', []),
    'F': ('OR', []),
    'G': ('OR', [])
}

heuristica_ao = {
    'A': 10, 'B': 6, 'C': 4,
    'D': 1, 'E': 2, 'F': 3, 'G': 1
}

def ao_estrella(nodo):
    print("[AO*] Evaluando:", nodo)

    tipo, hijos = grafo_ao[nodo]

    # nodo terminal
    if not hijos:
        return heuristica_ao[nodo], [nodo]

    if tipo == 'OR':
        mejor_costo = float('inf')
        mejor_camino = []

        for h in hijos:
            costo, camino = ao_estrella(h)

            if costo < mejor_costo:
                mejor_costo = costo
                mejor_camino = camino

        return mejor_costo, [nodo] + mejor_camino

    elif tipo == 'AND':
        total = 0
        camino_total = [nodo]

        for h in hijos:
            costo, camino = ao_estrella(h)
            total += costo
            camino_total += camino

        return total, camino_total


# =========================
#  EJECUCIÓN

print("\n===== A* =====")
camino, costo = a_estrella('A', 'G')
print("Camino A*:", camino)
print("Costo total:", costo)

print("\n===== AO* =====")
costo_ao, camino_ao = ao_estrella('A')
print("Solución AO*:", camino_ao)
print("Costo total:", costo_ao)