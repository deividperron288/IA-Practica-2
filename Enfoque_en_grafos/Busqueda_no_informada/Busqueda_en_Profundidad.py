# Grafo representado como diccionario
'''
        A
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

def dfs(nodo, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    
    print("Visitando:", nodo)
    visitados.add(nodo)
    
    if nodo == objetivo:
        print("¡Encontrado:", nodo, "!")
        return True
    
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            if dfs(vecino, objetivo, visitados):
                return True
    
    return False

# Buscar de A a G
dfs('A', 'G')