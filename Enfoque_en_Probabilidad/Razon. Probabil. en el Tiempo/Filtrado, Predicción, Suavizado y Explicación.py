import numpy as np

# Estados
estados = ["Soleado", "Lluvioso"]

# Matriz de transición
T = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# Matriz de observación
# [Paraguas, No paraguas]
O = np.array([
    [0.2, 0.8],  # Soleado
    [0.9, 0.1]   # Lluvioso
])

# Creencia inicial
belief = np.array([0.5, 0.5])

# Observaciones:
# 0 = paraguas
# 1 = no paraguas
observaciones = [0, 0, 1]

print("=== FILTRADO ===")

for obs in observaciones:

    # Predicción
    belief = T.T @ belief

    # Corrección con observación
    belief = belief * O[:, obs]

    # Normalización
    belief = belief / np.sum(belief)

    print("Probabilidades:")
    print("Soleado:", round(belief[0], 3))
    print("Lluvioso:", round(belief[1], 3))
    print()