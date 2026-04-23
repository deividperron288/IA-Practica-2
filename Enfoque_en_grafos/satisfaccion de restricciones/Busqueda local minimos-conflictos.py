import random

variables = ['A', 'B', 'C', 'D']

dominios = {
    v: ['Rojo', 'Verde', 'Azul'] for v in variables
}

vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# contar conflictos de una variable
def contar_conflictos(var, valor, asignacion):
    conflictos = 0
    for v in vecinos[var]:
        if asignacion[v] == valor:
            conflictos += 1
    return conflictos

def min_conflicts(max_iter=100):
    # asignación inicial aleatoria
    asignacion = {v: random.choice(dominios[v]) for v in variables}

    for i in range(max_iter):
        # encontrar variables en conflicto
        conflictos_vars = [
            v for v in variables
            if contar_conflictos(v, asignacion[v], asignacion) > 0
        ]

        if not conflictos_vars:
            return asignacion  # solución encontrada

        var = random.choice(conflictos_vars)

        # elegir valor con menos conflictos
        mejor_valor = min(
            dominios[var],
            key=lambda val: contar_conflictos(var, val, asignacion)
        )

        asignacion[var] = mejor_valor

        print(f"Iter {i}: {asignacion}")

    return None

# ejecutar
sol = min_conflicts()
print("\nSolución:", sol)