# Grafo representado como diccionario
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
    print(f"Visitando: {nodo}, profundidad: {profundidad}")
    
    # Si encontramos el objetivo
    if nodo == objetivo:
        print("¡Encontrado:", nodo, "!")
        return True
    
    # Si alcanzamos el límite, no seguimos bajando
    if profundidad == limite:
        return False
    
    # Explorar vecinos
    for vecino in grafo[nodo]:
        if dls(vecino, objetivo, limite, profundidad + 1):
            return True
    
    return False

# Ejemplo 1: límite suficiente
print("Búsqueda con límite = 2")
dls('A', 'G', 2)

print("\nBúsqueda con límite = 1")
# Ejemplo 2: límite insuficiente
dls('A', 'G', 1)