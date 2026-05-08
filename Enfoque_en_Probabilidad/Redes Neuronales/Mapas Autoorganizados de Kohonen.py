# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt


# =========================
# GENERAR DATOS
# =========================

np.random.seed(0)

datos = np.random.rand(200, 2)


# =========================
# PARÁMETROS SOM
# =========================

tam_mapa = 5

learning_rate = 0.5

epocas = 100


# =========================
# INICIALIZAR PESOS
# =========================

pesos = np.random.rand(
    tam_mapa,
    tam_mapa,
    2
)


# =========================
# ENTRENAMIENTO
# =========================

for epoca in range(epocas):

    for x in datos:

        # =====================
        # BUSCAR GANADOR
        # =====================

        distancias = np.linalg.norm(
            pesos - x,
            axis=2
        )

        ganador = np.unravel_index(
            np.argmin(distancias),
            distancias.shape
        )

        # =====================
        # ACTUALIZAR PESOS
        # =====================

        i, j = ganador

        pesos[i, j] += learning_rate * (x - pesos[i, j])


# =========================
# GRAFICAR RESULTADOS
# =========================

plt.figure(figsize=(7,7))

# Datos originales
plt.scatter(
    datos[:,0],
    datos[:,1],
    alpha=0.5
)

# Neuronas SOM
for i in range(tam_mapa):
    for j in range(tam_mapa):

        plt.scatter(
            pesos[i,j,0],
            pesos[i,j,1],
            marker='X',
            s=200
        )

plt.title("Mapa Autoorganizado de Kohonen")

plt.show()