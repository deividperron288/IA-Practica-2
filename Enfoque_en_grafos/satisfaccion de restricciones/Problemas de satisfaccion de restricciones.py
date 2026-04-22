# variables (nodos)
variables = ['A', 'B', 'C', 'D']

# dominios (colores posibles)
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul']
}

# grafo (restricciones)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# verificar restricciones
def es_valido(variable, valor, asignacion):
    for vecino in vecinos[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# backtracking
def backtracking(asignacion):
    # si ya asignamos todas las variables
    if len(asignacion) == len(variables):
        return asignacion

    # elegir variable no asignada
    for var in variables:
        if var not in asignacion:
            break

    # probar valores
    for valor in dominios[var]:
        if es_valido(var, valor, asignacion):
            asignacion[var] = valor

            resultado = backtracking(asignacion)
            if resultado:
                return resultado

            # backtrack
            del asignacion[var]

    return None

# ejecutar
solucion = backtracking({})
print("Solución:", solucion)