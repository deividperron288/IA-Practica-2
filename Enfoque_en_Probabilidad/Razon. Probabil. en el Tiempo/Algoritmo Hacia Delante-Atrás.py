import numpy as np

# Estados
estados = ["Soleado", "Lluvioso"]

# Matriz de transición
T = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# Matriz de observación
# Columnas:
# 0 = Paraguas
# 1 = No paraguas
O = np.array([
    [0.2, 0.8],  # Soleado
    [0.9, 0.1]   # Lluvioso
])

# Observaciones
observaciones = [0, 0, 1]

# Cantidad de estados
N = 2

# Cantidad de observaciones
T_obs = len(observaciones)

# Probabilidad inicial
pi = np.array([0.5, 0.5])

# =========================
# FORWARD
# =========================

alpha = np.zeros((T_obs, N))

# Inicialización
alpha[0] = pi * O[:, observaciones[0]]

# Normalizar
alpha[0] /= np.sum(alpha[0])

# Recursión forward
for t in range(1, T_obs):

    for j in range(N):

        alpha[t, j] = O[j, observaciones[t]] * np.sum(
            alpha[t-1] * T[:, j]
        )

    # Normalizar
    alpha[t] /= np.sum(alpha[t])

# =========================
# BACKWARD
# =========================

beta = np.zeros((T_obs, N))

# Inicialización
beta[-1] = 1

# Recursión backward
for t in range(T_obs - 2, -1, -1):

    for i in range(N):

        beta[t, i] = np.sum(
            T[i] *
            O[:, observaciones[t+1]] *
            beta[t+1]
        )

    # Normalizar
    beta[t] /= np.sum(beta[t])

# =========================
# SUAVIZADO
# =========================

posterior = alpha * beta

# Normalizar
posterior /= posterior.sum(axis=1, keepdims=True)

# Mostrar resultados
for t in range(T_obs):

    print(f"\nTiempo {t+1}")

    print("Soleado:", round(posterior[t, 0], 3))
    print("Lluvioso:", round(posterior[t, 1], 3))