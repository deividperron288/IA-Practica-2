import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# =========================
# Movimiento real
# =========================

n = 30

posicion_real = []

x_real = 0

for _ in range(n):

    # Movimiento real
    x_real += 1 + np.random.normal(0, 0.5)

    posicion_real.append(x_real)

# =========================
# Mediciones ruidosas
# =========================

mediciones = [
    x + np.random.normal(0, 2)
    for x in posicion_real
]

# =========================
# FILTRO DE PARTÍCULAS
# =========================

num_particulas = 1000

# Inicializar partículas
particulas = np.random.uniform(-5, 5, num_particulas)

# Pesos iniciales
pesos = np.ones(num_particulas) / num_particulas

estimaciones = []

for z in mediciones:

    # =====================
    # PREDICCIÓN
    # =====================

    particulas += 1 + np.random.normal(0, 0.5, num_particulas)

    # =====================
    # ACTUALIZAR PESOS
    # =====================

    error = z - particulas

    pesos = np.exp(-(error**2) / 8)

    pesos += 1e-300

    pesos /= np.sum(pesos)

    # =====================
    # ESTIMACIÓN
    # =====================

    estimacion = np.sum(particulas * pesos)

    estimaciones.append(estimacion)

    # =====================
    # RESAMPLEO
    # =====================

    indices = np.random.choice(
        range(num_particulas),
        size=num_particulas,
        p=pesos
    )

    particulas = particulas[indices]

    pesos = np.ones(num_particulas) / num_particulas

# =========================
# GRAFICAR
# =========================

plt.plot(posicion_real, label="Posición real")

plt.scatter(
    range(n),
    mediciones,
    label="Mediciones"
)

plt.plot(
    estimaciones,
    label="Particle Filter"
)

plt.xlabel("Tiempo")
plt.ylabel("Posición")

plt.title("Filtrado de Partículas")

plt.legend()
plt.grid(True)

plt.show()