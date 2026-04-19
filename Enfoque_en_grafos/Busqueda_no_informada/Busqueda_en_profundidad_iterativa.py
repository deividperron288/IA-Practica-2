# Grafo como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(nodo, objetivo, limite, profundidad=0):
    if nodo == objetivo:
        return True
    
    if profundidad == limite:
        return False
    
    for vecino in grafo[nodo]:
        if dls(vecino, objetivo, limite, profundidad + 1):
            return True
    
    return False

def ids(inicio, objetivo, max_profundidad):
    for limite in range(max_profundidad + 1):
        print(f"\nIntentando con límite = {limite}")
        
        if dls(inicio, objetivo, limite):
            print(f"¡Encontrado {objetivo} con límite {limite}!")
            return True
    
    return False

# Ejecutar IDS
ids('A', 'G', 3)