import numpy as np

# =========================
# Clases
# =========================

clases = ["Spam", "No Spam"]

# =========================
# Probabilidades previas
# =========================

prior = np.array([0.4, 0.6])

# =========================
# Palabras observadas
# =========================

mensaje = ["gratis", "oferta"]

# =========================
# Modelo probabilístico
# P(palabra | clase)
# =========================

modelo = {
    "Spam": {
        "gratis": 0.8,
        "oferta": 0.7
    },

    "No Spam": {
        "gratis": 0.1,
        "oferta": 0.2
    }
}

# =========================
# Calcular probabilidades
# =========================

probabilidades = []

for i, clase in enumerate(clases):

    # Empezar con el prior
    prob = prior[i]

    # Multiplicar probabilidades
    for palabra in mensaje:

        prob *= modelo[clase][palabra]

    probabilidades.append(prob)

# =========================
# Normalizar
# =========================

probabilidades = np.array(probabilidades)

probabilidades /= np.sum(probabilidades)

# =========================
# Mostrar resultados
# =========================

for clase, prob in zip(clases, probabilidades):

    print(f"{clase}: {prob:.3f}")

# Clase final
indice = np.argmax(probabilidades)

print("\nClasificación final:")
print(clases[indice])