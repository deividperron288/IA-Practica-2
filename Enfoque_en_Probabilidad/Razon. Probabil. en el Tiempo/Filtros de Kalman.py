import numpy as np
import matplotlib.pyplot as plt

# Reproducibilidad
np.random.seed(0)

# =========================
# Movimiento real
# =========================

n = 50

posicion_real = np.arange(n)

# Mediciones con ruido
mediciones = posicion_real + np.random.normal(0, 2, n)

# =========================
# Filtro de Kalman
# =========================

# Estado inicial
x = 0

# Incertidumbre inicial
P = 1

# Ruido del proceso
Q = 0.1

# Ruido del sensor
R = 4

# Lista de estimaciones
estimaciones = []

for z in mediciones:

    # =====================
    # PREDICCIÓN
    # =====================

    x_pred = x
    P_pred = P + Q

    # =====================
    # CORRECCIÓN
    # =====================

    # Ganancia de Kalman
    K = P_pred / (P_pred + R)

    # Actualizar estado
    x = x_pred + K * (z - x_pred)

    # Actualizar incertidumbre
    P = (1 - K) * P_pred

    estimaciones.append(x)

# =========================
# Graficar
# =========================

plt.plot(posicion_real, label="Posición real")
plt.scatter(range(n), mediciones, label="Mediciones")
plt.plot(estimaciones, label="Kalman")

plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.title("Filtro de Kalman")
plt.grid(True)

plt.show()