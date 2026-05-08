# ======================================
# COMPARACIÓN DE REDES NEURONALES
# HAMMING - HEBB - HOPFIELD - BOLTZMANN
# ======================================

import numpy as np
import matplotlib.pyplot as plt


# ======================================
# DATOS DE EJEMPLO
# ======================================

# Patrón original
patron = np.array([1, -1, 1, -1])

# Patrón con ruido
entrada_ruido = np.array([1, -1, -1, -1])

print("Patrón original:")
print(patron)

print("\nPatrón con ruido:")
print(entrada_ruido)


# ======================================
# 1. HAMMING
# ======================================

print("\n==============================")
print("RED DE HAMMING")
print("==============================")

# Convertir a binario para comparación
p1 = (patron == 1).astype(int)
p2 = (entrada_ruido == 1).astype(int)

distancia_hamming = np.sum(p1 != p2)

print("Distancia de Hamming:", distancia_hamming)


# ======================================
# 2. REGLA DE HEBB
# ======================================

print("\n==============================")
print("REGLA DE HEBB")
print("==============================")

# Inicializar pesos
W_hebb = np.zeros((4,4))

# Aprendizaje Hebb
for i in range(4):
    for j in range(4):
        W_hebb[i,j] = patron[i] * patron[j]

# Eliminar autoconexiones
np.fill_diagonal(W_hebb, 0)

print("Matriz de pesos Hebb:")
print(W_hebb)


# ======================================
# 3. RED DE HOPFIELD
# ======================================

print("\n==============================")
print("RED DE HOPFIELD")
print("==============================")

# Recuperar patrón
salida_hopfield = np.sign(W_hebb @ entrada_ruido)

print("Patrón recuperado:")
print(salida_hopfield)


# ======================================
# 4. BOLTZMANN
# ======================================

print("\n==============================")
print("MÁQUINA DE BOLTZMANN")
print("==============================")

# Función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Activación probabilística
activaciones = sigmoid(salida_hopfield)

print("Probabilidades de activación:")
print(activaciones)


# ======================================
# VISUALIZACIÓN
# ======================================

fig, ax = plt.subplots(1, 4, figsize=(14,4))

# Original
ax[0].imshow(patron.reshape(2,2), cmap='gray')
ax[0].set_title("Original")

# Ruido
ax[1].imshow(entrada_ruido.reshape(2,2), cmap='gray')
ax[1].set_title("Con Ruido")

# Hopfield
ax[2].imshow(salida_hopfield.reshape(2,2), cmap='gray')
ax[2].set_title("Hopfield")

# Boltzmann
ax[3].imshow(activaciones.reshape(2,2), cmap='gray')
ax[3].set_title("Boltzmann")

plt.tight_layout()
plt.show()