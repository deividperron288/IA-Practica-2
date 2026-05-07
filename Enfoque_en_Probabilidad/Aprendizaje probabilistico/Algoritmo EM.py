import numpy as np
import matplotlib.pyplot as plt

# =========================
# Datos
# =========================

X = np.array([1, 2, 3, 8, 9, 10])

# =========================
# Inicialización
# =========================

# Medias iniciales
mu1 = 2
mu2 = 9

# Varianza fija
sigma = 1.5

# Probabilidades iniciales
pi1 = 0.5
pi2 = 0.5

# Cantidad de iteraciones
iteraciones = 10

# =========================
# Función gaussiana
# =========================

def gauss(x, mu, sigma):

    return (
        1 / np.sqrt(2 * np.pi * sigma**2)
    ) * np.exp(
        -(x - mu)**2 / (2 * sigma**2)
    )

# =========================
# Algoritmo EM
# =========================

for iteracion in range(iteraciones):

    # =====================
    # E-STEP
    # =====================

    r1 = pi1 * gauss(X, mu1, sigma)
    r2 = pi2 * gauss(X, mu2, sigma)

    total = r1 + r2

    # Responsabilidades
    r1 /= total
    r2 /= total

    # =====================
    # M-STEP
    # =====================

    mu1 = np.sum(r1 * X) / np.sum(r1)
    mu2 = np.sum(r2 * X) / np.sum(r2)

    pi1 = np.mean(r1)
    pi2 = np.mean(r2)

    # =====================
    # Mostrar resultados
    # =====================

    print(f"\nIteración {iteracion+1}")

    print("Media grupo 1:", round(mu1, 3))
    print("Media grupo 2:", round(mu2, 3))

# =========================
# Graficar datos
# =========================

plt.scatter(X, np.zeros_like(X))

plt.axvline(mu1, linestyle="--", label="Grupo 1")
plt.axvline(mu2, linestyle="--", label="Grupo 2")

plt.legend()

plt.title("Algoritmo EM")
plt.show()