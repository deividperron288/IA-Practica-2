# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.linear_model import Perceptron


# =========================
# GENERAR DATOS
# =========================

X, y = make_blobs(
    n_samples=100,
    centers=2,
    cluster_std=1.0,
    random_state=0
)


# =========================
# CREAR PERCEPTRÓN
# =========================

modelo = Perceptron()

# Entrenar
modelo.fit(X, y)


# =========================
# OBTENER PESOS
# =========================

w = modelo.coef_[0]
b = modelo.intercept_[0]

print("Pesos:", w)
print("Bias:", b)


# =========================
# CREAR FRONTERA DE DECISIÓN
# =========================

x_linea = np.linspace(X[:,0].min(), X[:,0].max(), 100)

y_linea = -(w[0] * x_linea + b) / w[1]


# =========================
# GRAFICAR
# =========================

plt.figure(figsize=(8,6))

# Puntos
plt.scatter(
    X[:,0],
    X[:,1],
    c=y,
    cmap='coolwarm'
)

# Línea separadora
plt.plot(x_linea, y_linea)

plt.title("Separabilidad Lineal")
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()