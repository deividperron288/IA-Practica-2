import heapq

# Grafo con costos (nodo: [(vecino, costo)])
'''
        A
      /   \
     B     C
    / \   / \
   D   E F   G
'''
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def ucs(inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))  # (costo, nodo)
    
    visitados = set()
    
    while cola:
        costo, nodo = heapq.heappop(cola)
        
        if nodo in visitados:
            continue
        
        print(f"Visitando: {nodo} con costo {costo}")
        visitados.add(nodo)
        
        if nodo == objetivo:
            print(f"¡Encontrado {nodo} con costo total {costo}!")
            return costo
        
        for vecino, peso in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(cola, (costo + peso, vecino))
    
    return None

# Buscar de A a G
ucs('A', 'G')