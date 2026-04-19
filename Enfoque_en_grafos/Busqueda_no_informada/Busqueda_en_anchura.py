from collections import deque

# Representación del árbol como grafo (diccionario)
'''     A
      /   \
     B     C
    / \   / \
   D   E F   G
'''
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(inicio, objetivo):
    cola = deque([inicio])  # Cola
    visitados = set()       # Nodos visitados

    while cola:
        nodo = cola.popleft()
        
        if nodo not in visitados:
            print("Visitando:", nodo)
            visitados.add(nodo)

            if nodo == objetivo:
                print("¡Encontrado:", nodo, "!")
                return True

            # Agregar vecinos a la cola
            cola.extend(grafo[nodo])
    
    return False

# Ejecutar búsqueda de A a G
bfs('A', 'G')