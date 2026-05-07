import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =========================
# GENERAR DATOS
# =========================

# Creamos datos en forma de medias lunas
X, y = make_moons(n_samples=300, noise=0.2, random_state=0)

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=0
)


# =========================
# CREAR RED NEURONAL
# =========================

modelo = MLPClassifier(
    hidden_layer_sizes=(8, 8),  # Dos capas ocultas con 8 neuronas
    activation='relu',          # Función de activación
    solver='adam',              # Algoritmo de aprendizaje
    max_iter=5000,
    random_state=0
)


# =========================
# ENTRENAR MODELO
# =========================

modelo.fit(X_train, y_train)


# =========================
# HACER PREDICCIONES
# =========================

predicciones = modelo.predict(X_test)


# =========================
# EVALUAR RESULTADOS
# =========================

precision = accuracy_score(y_test, predicciones)

print("Precisión del modelo:", precision)


# =========================
# GRAFICAR RESULTADOS
# =========================

plt.figure(figsize=(8, 6))

# Dibujar puntos
plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=predicciones,
    cmap='coolwarm'
)

plt.title("Clasificación usando Red Neuronal")
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()