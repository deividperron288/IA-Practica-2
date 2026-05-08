# =========================
# IMPORTAR LIBRERÍAS
# =========================

import numpy as np
import matplotlib.pyplot as plt


# =========================
# DATOS XOR
# =========================

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])


# =========================
# FUNCIÓN SIGMOIDE
# =========================

def sigmoide(x):
    return 1 / (1 + np.exp(-x))


# Derivada de sigmoide
def derivada_sigmoide(x):
    return x * (1 - x)


# =========================
# INICIALIZAR PESOS
# =========================

np.random.seed(0)

# Entrada -> capa oculta
W1 = np.random.randn(2, 2)

# Capa oculta -> salida
W2 = np.random.randn(2, 1)

learning_rate = 0.1

errores = []


# =========================
# ENTRENAMIENTO
# =========================

for epoca in range(10000):

    # =====================
    # FORWARD PROPAGATION
    # =====================

    hidden_input = np.dot(X, W1)
    hidden_output = sigmoide(hidden_input)

    final_input = np.dot(hidden_output, W2)
    final_output = sigmoide(final_input)


    # =====================
    # ERROR
    # =====================

    error = y - final_output

    mse = np.mean(error**2)

    errores.append(mse)


    # =====================
    # BACKPROPAGATION
    # =====================

    d_output = error * derivada_sigmoide(final_output)

    error_hidden = d_output.dot(W2.T)

    d_hidden = error_hidden * derivada_sigmoide(hidden_output)


    # =====================
    # ACTUALIZAR PESOS
    # =====================

    W2 += hidden_output.T.dot(d_output) * learning_rate

    W1 += X.T.dot(d_hidden) * learning_rate


# =========================
# RESULTADOS
# =========================

print("Salida final:")

print(final_output)


# =========================
# GRAFICAR ERROR
# =========================

plt.plot(errores)

plt.title("Retropropagación del Error")
plt.xlabel("Época")
plt.ylabel("MSE")

plt.show()