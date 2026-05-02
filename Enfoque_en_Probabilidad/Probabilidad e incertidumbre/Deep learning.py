import numpy as np
from sklearn.neural_network import MLPClassifier

# 1. Generar datos
np.random.seed(0)
X = np.random.rand(100, 2)

# Regla: x + y > 1 → clase 1
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# 2. Crear modelo (red neuronal)
model = MLPClassifier(hidden_layer_sizes=(8,),
                      activation='relu',
                      max_iter=500)

# 3. Entrenar
model.fit(X, y)

# 4. Probar con nuevo dato
nuevo = np.array([[0.8, 0.5]])

prob = model.predict_proba(nuevo)

print("Probabilidades [clase 0, clase 1]:", prob)