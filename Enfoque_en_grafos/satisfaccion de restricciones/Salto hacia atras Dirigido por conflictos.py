variables = ['A', 'B', 'C']

dominios = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1, 2]
}

# restricciones: todos diferentes
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

def es_valido(var, val, asignacion):
    conflictos = set()

    for v in vecinos[var]:
        if v in asignacion and asignacion[v] == val:
            conflictos.add(v)

    return (len(conflictos) == 0, conflictos)

def cbj(asignacion, nivel):
    if nivel == len(variables):
        return asignacion, set()

    var = variables[nivel]
    conflictos_total = set()

    for valor in dominios[var]:
        valido, conflictos = es_valido(var, valor, asignacion)

        if valido:
            asignacion[var] = valor
            resultado, conflictos_hijo = cbj(asignacion, nivel + 1)

            if resultado:
                return resultado, set()

            if var not in conflictos_hijo:
                return None, conflictos_hijo

            conflictos_total.update(conflictos_hijo)
            del asignacion[var]
        else:
            conflictos_total.update(conflictos)

    conflictos_total.add(var)
    return None, conflictos_total

# ejecutar
solucion, _ = cbj({}, 0)
print("Solución:", solucion)