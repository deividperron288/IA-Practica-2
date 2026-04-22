# variables
variables = ['A', 'B', 'C']

# dominios
dominios = {
    'A': ['Rojo', 'Verde'],
    'B': ['Rojo', 'Verde'],
    'C': ['Rojo', 'Verde']
}

# vecinos
vecinos = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

def forward_checking(asignacion, dominios):
    if len(asignacion) == len(variables):
        return asignacion

    # elegir variable no asignada
    for var in variables:
        if var not in asignacion:
            break

    for valor in dominios[var]:
        # copia de dominios
        nuevos_dominios = {v: list(dominios[v]) for v in dominios}

        asignacion[var] = valor

        valido = True

        # 🔥 forward checking
        for vecino in vecinos[var]:
            if vecino not in asignacion:
                if valor in nuevos_dominios[vecino]:
                    nuevos_dominios[vecino].remove(valor)

                # si se queda sin opciones → fallo temprano
                if not nuevos_dominios[vecino]:
                    valido = False
                    break

        if valido:
            resultado = forward_checking(asignacion, nuevos_dominios)
            if resultado:
                return resultado

        # backtrack
        del asignacion[var]

    return None

# ejecutar
sol = forward_checking({}, dominios)
print("Solución:", sol)