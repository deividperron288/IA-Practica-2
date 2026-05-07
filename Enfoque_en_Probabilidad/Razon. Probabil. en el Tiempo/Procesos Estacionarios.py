import numpy as np
import matplotlib.pyplot as plt

# Para resultados reproducibles
np.random.seed(0)

# Cantidad de datos
n = 100

# Crear arreglo
X = np.zeros(n)

# Generar ruido aleatorio
ruido = np.random.normal(0, 1, n)

# Proceso AR(1)
for t in range(1, n):
    X[t] = 0.8 * X[t-1] + ruido[t]

# Graficar
plt.plot(X)
plt.title("Proceso Estacionario AR(1)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()

# Media y varianza
print("Media:", np.mean(X))
print("Varianza:", np.var(X))