import numpy as np

# Para reproducibilidad
np.random.seed(0)

# Estados posibles
estados = ["Soleado", "Lluvioso"]

# Matriz de transición
# Filas = estado actual
# Columnas = siguiente estado
transicion = np.array([
    [0.8, 0.2],  # Soleado
    [0.4, 0.6]   # Lluvioso
])

# Estado inicial
estado_actual = 0  # Soleado

# Simulación
dias = 10

print("Día 1:", estados[estado_actual])

for dia in range(1, dias):

    # Elegir siguiente estado según probabilidades
    estado_actual = np.random.choice(
        [0, 1],
        p=transicion[estado_actual]
    )

    print(f"Día {dia+1}: {estados[estado_actual]}")