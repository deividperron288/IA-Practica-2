from sklearn.naive_bayes import GaussianNB
import numpy as np

# Datos de ejemplo (altura, peso)
X = np.array([
    [170, 65],
    [160, 55],
    [180, 80],
    [175, 75]
])

# Clases: 0 = no atleta, 1 = atleta
y = np.array([0, 0, 1, 1])

# Crear modelo
model = GaussianNB()

# Entrenar modelo
model.fit(X, y)

# Nuevo dato
nuevo = np.array([[172, 70]])

# Predicción
pred = model.predict(nuevo)

print("Clase predicha:", pred)