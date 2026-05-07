import numpy as np

# =========================
# Palabras posibles
# =========================

palabras = ["Hola", "Adiós"]

# =========================
# Observaciones acústicas
# =========================

# Supongamos:
# 0 = sonido grave
# 1 = sonido medio
# 2 = sonido agudo

observaciones = [0, 1, 1]

# =========================
# Probabilidades iniciales
# =========================

P_palabras = np.array([0.6, 0.4])

# =========================
# Modelo acústico
# P(sonido | palabra)
# =========================

# Filas:
# Hola, Adiós

# Columnas:
# grave, medio, agudo

modelo_acustico = np.array([
    [0.5, 0.4, 0.1],  # Hola
    [0.2, 0.3, 0.5]   # Adiós
])

# =========================
# Calcular probabilidades
# =========================

probabilidades = []

for i, palabra in enumerate(palabras):

    prob = P_palabras[i]

    for obs in observaciones:

        prob *= modelo_acustico[i, obs]

    probabilidades.append(prob)

# =========================
# Normalizar
# =========================

probabilidades = np.array(probabilidades)

probabilidades /= np.sum(probabilidades)

# =========================
# Resultados
# =========================

for palabra, prob in zip(palabras, probabilidades):

    print(f"{palabra}: {prob:.3f}")

# Palabra más probable
indice = np.argmax(probabilidades)

print("\nReconocimiento final:")
print(palabras[indice])