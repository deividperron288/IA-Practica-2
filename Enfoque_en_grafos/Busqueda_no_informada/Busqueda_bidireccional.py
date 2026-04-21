from collections import deque

# Grafo no dirigido corregido
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G', 'H'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C'],
    'H': ['C']
}

def busqueda_bidireccional(inicio, objetivo):
    if inicio == objetivo:
        return True

    cola_inicio = deque([inicio])
    cola_objetivo = deque([objetivo])

    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    while cola_inicio and cola_objetivo:
        # Desde inicio
        nodo_i = cola_inicio.popleft()
        print("Desde inicio:", nodo_i)

        for vecino in grafo[nodo_i]:
            if vecino not in visitados_inicio:
                visitados_inicio.add(vecino)
                cola_inicio.append(vecino)

                if vecino in visitados_objetivo:
                    print("¡Se encontraron en:", vecino, "!")
                    return True

        # Desde objetivo
        nodo_o = cola_objetivo.popleft()
        print("Desde objetivo:", nodo_o)

        for vecino in grafo[nodo_o]:
            if vecino not in visitados_objetivo:
                visitados_objetivo.add(vecino)
                cola_objetivo.append(vecino)

                if vecino in visitados_inicio:
                    print("¡Se encontraron en:", vecino, "!")
                    return True

    return False

# Buscar de A a H
busqueda_bidireccional('A', 'H')