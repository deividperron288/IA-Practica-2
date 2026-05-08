import numpy as np
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons


# =========================
# DATOS
# =========================

X, y = make_moons(
    n_samples=300,
    noise=0.2,
    random_state=0
)


# =========================
# RED TIPO MADALINE
# =========================

modelo = MLPClassifier(
    hidden_layer_sizes=(5, 5),
    activation='relu',
    max_iter=5000,
    random_state=0
)


# =========================
# ENTRENAR
# =========================

modelo.fit(X, y)


# =========================
# PREDICCIONES
# =========================

predicciones = modelo.predict(X)


# =========================
# GRAFICAR
# =========================

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=predicciones,
    cmap='coolwarm'
)

plt.title("Red multicapa tipo MADALINE")

plt.show()