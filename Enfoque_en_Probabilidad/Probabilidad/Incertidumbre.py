import numpy as np

# Probabilidades de un modelo (ejemplo)
probs_seguro = np.array([0.9, 0.1])   # bastante seguro
probs_inseguro = np.array([0.5, 0.5]) # muy incierto

# Función de entropía
def entropia(p):
    return -np.sum(p * np.log2(p + 1e-9))  # evitamos log(0)

# Calcular incertidumbre
H_seguro = entropia(probs_seguro)
H_inseguro = entropia(probs_inseguro)

print("Entropía (caso seguro):", H_seguro)
print("Entropía (caso incierto):", H_inseguro)