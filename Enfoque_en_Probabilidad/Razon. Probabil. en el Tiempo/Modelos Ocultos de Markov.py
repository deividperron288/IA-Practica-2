import numpy as np

# =========================
# Estados ocultos
# =========================

estados = ["Soleado", "Lluvioso"]

# =========================
# Observaciones
# =========================

observaciones_texto = ["Paraguas", "Paraguas", "No paraguas"]

# Codificación:
# 0 = Paraguas
# 1 = No paraguas

observaciones = [0, 0, 1]

# =========================
# Probabilidades iniciales
# =========================

pi = np.array([0.5, 0.5])

# =========================
# Matriz de transición
# =========================

T = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# =========================
# Matriz de emisión
# =========================

O = np.array([
    [0.2, 0.8],  # Soleado
    [0.9, 0.1]   # Lluvioso
])

# =========================
# FILTRADO
# =========================

belief = pi

for t, obs in enumerate(observaciones):

    # Predicción
    belief = T.T @ belief

    # Corrección usando observación
    belief = belief * O[:, obs]

    # Normalización
    belief = belief / np.sum(belief)

    print(f"\nTiempo {t+1}")
    print("Observación:", observaciones_texto[t])

    print("P(Soleado):", round(belief[0], 3))
    print("P(Lluvioso):", round(belief[1], 3))