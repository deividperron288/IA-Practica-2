import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Generar datos
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 puntos (x, y)

# Regla: x + y > 1 → clase 1
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# 2. Crear modelo
model = keras.Sequential([
    layers.Dense(8, activation='relu', input_shape=(2,)),
    layers.Dense(1, activation='sigmoid')
])

# 3. Compilar
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 4. Entrenar
model.fit(X, y, epochs=50, verbose=0)

# 5. Probar con un nuevo dato
nuevo = np.array([[0.8, 0.5]])  # x+y=1.3 → debería ser clase 1
pred = model.predict(nuevo)

print("Probabilidad de clase 1:", pred[0][0])