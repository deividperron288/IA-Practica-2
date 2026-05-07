import numpy as np

from sklearn.neural_network import MLPClassifier

# =========================
# Datos XOR
# =========================

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    0,
    1,
    1,
    0
])

# =========================
# Crear red neuronal
# =========================

modelo = MLPClassifier(

    hidden_layer_sizes=(4,),
    activation='relu',
    max_iter=5000,
    random_state=0
)

# =========================
# Entrenar
# =========================

modelo.fit(X, y)

# =========================
# Predicciones
# =========================

predicciones = modelo.predict(X)

# =========================
# Mostrar resultados
# =========================

print("Predicciones:\n")

for entrada, pred in zip(X, predicciones):

    print(f"{entrada} -> {pred}")