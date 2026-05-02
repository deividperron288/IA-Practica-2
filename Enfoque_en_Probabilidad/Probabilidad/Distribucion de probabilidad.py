import numpy as np
import matplotlib.pyplot as plt

# 1. Simular lanzamientos de un dado
np.random.seed(0)
lanzamientos = np.random.randint(1, 7, size=1000)

# 2. Contar frecuencias
valores, conteos = np.unique(lanzamientos, return_counts=True)

# 3. Convertir a probabilidades
probabilidades = conteos / np.sum(conteos)

print("Valores:", valores)
print("Probabilidades:", probabilidades)

# 4. Graficar
plt.bar(valores, probabilidades)
plt.xlabel("Valor del dado")
plt.ylabel("Probabilidad")
plt.title("Distribución de probabilidad de un dado")
plt.show()