from collections import deque

# variables
variables = ['A', 'B', 'C']

# dominios
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# restricciones: todos deben ser diferentes
vecinos = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

# función para verificar consistencia
def es_consistente(x, y):
    return x != y

# AC-3
def ac3():
    cola = deque()

    # agregar todos los arcos
    for x in vecinos:
        for y in vecinos[x]:
            cola.append((x, y))

    while cola:
        (x, y) = cola.popleft()

        if revisar(x, y):
            if not dominios[x]:
                return False

            for z in vecinos[x]:
                if z != y:
                    cola.append((z, x))

    return True

# revisar y reducir dominio
def revisar(x, y):
    cambiado = False

    for valor_x in dominios[x][:]:
        # si no hay ningún valor compatible en y → eliminar
        if not any(es_consistente(valor_x, valor_y) for valor_y in dominios[y]):
            dominios[x].remove(valor_x)
            cambiado = True

    return cambiado

# ejecutar
print("Dominios antes:", dominios)
ac3()
print("Dominios después:", dominios)