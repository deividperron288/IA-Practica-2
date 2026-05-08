import numpy as np
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# ==========================================
# 1. CREAR EL CORPUS
# ==========================================

corpus = """
la inteligencia artificial aprende patrones
la inteligencia artificial procesa lenguaje
el lenguaje natural es importante
la inteligencia aprende del corpus
el corpus contiene palabras y frases
"""

# ==========================================
# 2. PREPROCESAMIENTO
# ==========================================

# Convertir a minúsculas y dividir palabras
palabras = corpus.lower().split()

print("Palabras del corpus:\n")
print(palabras)

# ==========================================
# 3. CONTAR FRECUENCIA DE PALABRAS
# ==========================================

frecuencia = Counter(palabras)

print("\nFrecuencia de palabras:\n")
for palabra, conteo in frecuencia.items():
    print(f"{palabra}: {conteo}")

# ==========================================
# 4. CALCULAR PROBABILIDADES
# ==========================================

total_palabras = len(palabras)

print("\nProbabilidades:\n")

probabilidades = {}

for palabra, conteo in frecuencia.items():
    prob = conteo / total_palabras
    probabilidades[palabra] = prob
    print(f"P({palabra}) = {prob:.3f}")

# ==========================================
# 5. MODELO BIGRAMA
# ==========================================

# Diccionario:
# palabra_actual -> siguiente_palabra

bigramas = defaultdict(list)

for i in range(len(palabras) - 1):
    actual = palabras[i]
    siguiente = palabras[i + 1]

    bigramas[actual].append(siguiente)

# ==========================================
# 6. MOSTRAR TRANSICIONES
# ==========================================

print("\nBigramas encontrados:\n")

for palabra, siguientes in bigramas.items():
    print(f"{palabra} -> {siguientes}")

# ==========================================
# 7. PREDICCIÓN SIMPLE
# ==========================================

def predecir_siguiente(palabra):
    
    if palabra not in bigramas:
        return "No existe en el corpus"

    siguientes = bigramas[palabra]

    # Contar frecuencia de siguientes palabras
    conteo = Counter(siguientes)

    # Elegir la más común
    prediccion = conteo.most_common(1)[0][0]

    return prediccion

# Probar predicción
entrada = "inteligencia"

resultado = predecir_siguiente(entrada)

print(f"\nDespués de '{entrada}' probablemente viene '{resultado}'")

# ==========================================
# 8. VISUALIZAR FRECUENCIAS
# ==========================================

plt.figure(figsize=(10,5))

plt.bar(frecuencia.keys(), frecuencia.values())

plt.title("Frecuencia de palabras en el corpus")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")

plt.xticks(rotation=45)

plt.show()