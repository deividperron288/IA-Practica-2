import numpy as np
from sklearn.linear_model import LogisticRegression

# 1. Generar datos
np.random.seed(0)
X = np.random.rand(100, 2)

# Regla: x + y > 1 → clase 1
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# 2. Crear modelo
model = LogisticRegression()

# 3. Entrenar
model.fit(X, y)

# 4. Probar con un nuevo punto
nuevo = np.array([[0.6, 0.6]])

probabilidades = model.predict_proba(nuevo)

print("Probabilidades [clase 0, clase 1]:", probabilidades)