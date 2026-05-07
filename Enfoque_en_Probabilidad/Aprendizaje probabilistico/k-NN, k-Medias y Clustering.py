import numpy as np
import matplotlib.pyplot as plt

# =========================
# Datos de entrenamiento
# =========================

X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [8, 8],
    [9, 8],
    [8, 9]
])

# Etiquetas
y = np.array([
    0, 0, 0,
    1, 1, 1
])

# Punto nuevo
nuevo = np.array([3, 2])

# =========================
# Calcular distancias
# =========================

distancias = np.linalg.norm(X - nuevo, axis=1)

# Ordenar vecinos
indices = np.argsort(distancias)

# Elegir k vecinos
k = 3

vecinos = y[indices[:k]]

# Votación
prediccion = np.bincount(vecinos).argmax()

print("Clase predicha:", prediccion)

# =========================
# Graficar
# =========================

for clase in [0, 1]:

    puntos = X[y == clase]

    plt.scatter(
        puntos[:, 0],
        puntos[:, 1],
        label=f"Clase {clase}"
    )

plt.scatter(
    nuevo[0],
    nuevo[1],
    s=200,
    marker="X",
    label="Nuevo punto"
)

plt.legend()
plt.grid(True)
plt.title("k-NN")

plt.show()
