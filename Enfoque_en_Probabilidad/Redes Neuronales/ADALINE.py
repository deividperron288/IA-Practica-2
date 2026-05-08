# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt


# =========================
# DATOS
# =========================

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([-1, -1, -1, 1])


# =========================
# INICIALIZAR PESOS
# =========================

pesos = np.random.randn(2)
bias = np.random.randn()

learning_rate = 0.1
epocas = 20

errores = []


# =========================
# ENTRENAMIENTO
# =========================

for epoca in range(epocas):

    error_total = 0

    for i in range(len(X)):

        # Salida lineal
        salida = np.dot(X[i], pesos) + bias

        # Error
        error = y[i] - salida

        # Ajustar pesos
        pesos += learning_rate * error * X[i]

        bias += learning_rate * error

        error_total += error**2

    errores.append(error_total)


# =========================
# GRAFICAR ERROR
# =========================

plt.plot(errores)

plt.title("Error en ADALINE")
plt.xlabel("Época")
plt.ylabel("Error Cuadrático")

plt.show()