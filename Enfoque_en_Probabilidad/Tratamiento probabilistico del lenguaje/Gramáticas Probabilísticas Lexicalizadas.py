import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# ==========================================
# 1. CORPUS DE ENTRENAMIENTO
# ==========================================

corpus = [

    ("perro", "come", "carne"),
    ("gato", "come", "pescado"),
    ("niño", "come", "manzana"),

    ("piedra", "rompe", "vidrio"),
    ("martillo", "rompe", "madera"),

    ("ave", "vuela", "cielo"),
]

# ==========================================
# 2. CONTAR RELACIONES LÉXICAS
# ==========================================

# sujeto -> verbo

relaciones = defaultdict(int)

# conteo total de verbos
conteo_verbos = defaultdict(int)

for sujeto, verbo, objeto in corpus:

    relaciones[(sujeto, verbo)] += 1
    conteo_verbos[verbo] += 1

# ==========================================
# 3. CALCULAR PROBABILIDADES
# ==========================================

probabilidades = {}

for (sujeto, verbo), frecuencia in relaciones.items():

    prob = frecuencia / conteo_verbos[verbo]

    probabilidades[(sujeto, verbo)] = prob

# ==========================================
# 4. MOSTRAR PROBABILIDADES
# ==========================================

print("PROBABILIDADES LEXICALIZADAS\n")

for clave, prob in probabilidades.items():

    sujeto, verbo = clave

    print(f"P({sujeto} | {verbo}) = {prob:.3f}")

# ==========================================
# 5. EVALUAR ORACIONES
# ==========================================

def evaluar_oracion(sujeto, verbo):

    if (sujeto, verbo) in probabilidades:
        return probabilidades[(sujeto, verbo)]

    return 0.0001

# Oraciones
ejemplos = [

    ("perro", "come"),
    ("gato", "come"),
    ("piedra", "come"),
    ("martillo", "vuela")
]

print("\nEVALUACIÓN DE ORACIONES\n")

resultados = []

for sujeto, verbo in ejemplos:

    prob = evaluar_oracion(sujeto, verbo)

    resultados.append(prob)

    print(f"{sujeto} {verbo} -> Probabilidad: {prob:.4f}")

# ==========================================
# 6. VISUALIZACIÓN
# ==========================================

etiquetas = [f"{s} {v}" for s, v in ejemplos]

plt.figure(figsize=(10,5))

plt.bar(etiquetas, resultados)

plt.title("Probabilidades de relaciones léxicas")
plt.xlabel("Oraciones")
plt.ylabel("Probabilidad")

plt.show()