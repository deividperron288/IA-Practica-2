import numpy as np
import matplotlib.pyplot as plt

# =========================
# Generar datos
# =========================

np.random.seed(0)

grupo1 = np.random.randn(50, 2) + [2, 2]
grupo2 = np.random.randn(50, 2) + [8, 8]

X = np.vstack((grupo1, grupo2))

# =========================
# Inicializar centroides
# =========================

k = 2

indices = np.random.choice(len(X), k, replace=False)

centroides = X[indices]

# =========================
# K-Means
# =========================

for iteracion in range(10):

    # =====================
    # Asignar clusters
    # =====================

    clusters = []

    for punto in X:

        distancias = np.linalg.norm(
            punto - centroides,
            axis=1
        )

        cluster = np.argmin(distancias)

        clusters.append(cluster)

    clusters = np.array(clusters)

    # =====================
    # Actualizar centroides
    # =====================

    nuevos_centroides = []

    for i in range(k):

        puntos_cluster = X[clusters == i]

        promedio = puntos_cluster.mean(axis=0)

        nuevos_centroides.append(promedio)

    centroides = np.array(nuevos_centroides)

# =========================
# Graficar resultados
# =========================

for i in range(k):

    puntos = X[clusters == i]

    plt.scatter(
        puntos[:, 0],
        puntos[:, 1],
        label=f"Cluster {i+1}"
    )

plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    s=200,
    marker="X",
    label="Centroides"
)

plt.title("Agrupamiento No Supervisado")
plt.legend()
plt.grid(True)

plt.show()