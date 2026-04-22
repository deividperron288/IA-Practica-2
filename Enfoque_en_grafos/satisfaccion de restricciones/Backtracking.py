# nodos del grafo
nodos = ['A', 'B', 'C', 'D']

# colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# restricciones (vecinos)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def es_valido(nodo, color, asignacion):
    for v in vecinos[nodo]:
        if v in asignacion and asignacion[v] == color:
            return False
    return True

def backtracking(asignacion):
    # si ya asignamos todo
    if len(asignacion) == len(nodos):
        return asignacion

    # elegir nodo sin asignar
    for nodo in nodos:
        if nodo not in asignacion:
            break

    # probar colores
    for color in colores:
        if es_valido(nodo, color, asignacion):
            asignacion[nodo] = color

            resultado = backtracking(asignacion)
            if resultado:
                return resultado

            # 👈 vuelta atrás (backtrack)
            del asignacion[nodo]

    return None

# ejecutar
solucion = backtracking({})
print("Solución:", solucion)