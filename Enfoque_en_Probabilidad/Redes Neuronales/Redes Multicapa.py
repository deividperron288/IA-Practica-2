# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =========================
# GENERAR DATOS
# =========================

X, y = make_moons(
    n_samples=300,
    noise=0.2,
    random_state=0
)


# =========================
# DIVIDIR DATOS
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)


# =========================
# CREAR RED MULTICAPA
# =========================

modelo = MLPClassifier(
    hidden_layer_sizes=(8, 8),
    activation='relu',
    solver='adam',
    max_iter=5000,
    random_state=0
)


# =========================
# ENTRENAR RED
# =========================

modelo.fit(X_train, y_train)


# =========================
# HACER PREDICCIONES
# =========================

predicciones = modelo.predict(X_test)


# =========================
# EVALUAR MODELO
# =========================

precision = accuracy_score(y_test, predicciones)

print("Precisión:", precision)


# =========================
# GRAFICAR RESULTADOS
# =========================

plt.figure(figsize=(8,6))

plt.scatter(
    X_test[:,0],
    X_test[:,1],
    c=predicciones,
    cmap='coolwarm'
)

plt.title("Clasificación con Red Multicapa")
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()