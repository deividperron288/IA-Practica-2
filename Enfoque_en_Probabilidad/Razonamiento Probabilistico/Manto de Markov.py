import numpy as np
from sklearn.feature_selection import mutual_info_classif

# Datos simulados
# A, B, C, D (como en red bayesiana conceptual)
X = np.array([
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]
])

# Queremos analizar la variable B (columna 1)
y = X[:, 1]

# Variables restantes (A, C, D)
X_features = np.delete(X, 1, axis=1)

# Calcular dependencia
mi = mutual_info_classif(X_features, y)

print("Importancia de variables (A, C, D):", mi)