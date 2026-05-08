# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =========================
# GENERAR DATOS
# =========================

X, y = make_blobs(
    n_samples=200,
    centers=2,
    random_state=0
)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=0
)


# =========================
# CREAR PERCEPTRÓN
# =========================

modelo = Perceptron(max_iter=1000)


# =========================
# ENTRENAR
# =========================

modelo.fit(X_train, y_train)


# =========================
# PREDICCIONES
# =========================

predicciones = modelo.predict(X_test)


# =========================
# EVALUAR
# =========================

precision = accuracy_score(y_test, predicciones)

print("Precisión:", precision)


# =========================
# GRAFICAR
# =========================

plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=predicciones,
    cmap='coolwarm'
)

plt.title("Clasificación con Perceptrón")
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()