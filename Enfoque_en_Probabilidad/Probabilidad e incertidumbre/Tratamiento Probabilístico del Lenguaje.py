from collections import defaultdict, Counter

# 1. Texto de ejemplo
texto = "me gusta el cafe me gusta el pan"

# 2. Convertir a lista de palabras
palabras = texto.split()

# 3. Contar bigramas
bigramas = defaultdict(Counter)

for i in range(len(palabras) - 1):
    palabra_actual = palabras[i]
    palabra_siguiente = palabras[i + 1]
    bigramas[palabra_actual][palabra_siguiente] += 1

# 4. Convertir a probabilidades
modelo = {}

for palabra, siguientes in bigramas.items():
    total = sum(siguientes.values())
    modelo[palabra] = {w: c / total for w, c in siguientes.items()}

# 5. Probar el modelo
entrada = "gusta"
print("Palabras probables después de 'gusta':")
print(modelo[entrada])