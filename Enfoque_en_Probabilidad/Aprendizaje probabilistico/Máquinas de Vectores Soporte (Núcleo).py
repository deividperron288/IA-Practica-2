import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC

# =========================
# Generar datos
# =========================

np.random.seed(0)

# Clase 0
X1 = np.random.randn(50, 2) + [0, 0]

# Clase 1
X2 = np.random.randn(50, 2) + [3, 3]

X = np.vstack((X1, X2))

y = np.array([0]*50 + [1]*50)

# =========================
# Crear SVM
# =========================

modelo = SVC(kernel="rbf")

# Entrenar
modelo.fit(X, y)

# =========================
# Crear malla para frontera
# =========================

x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

# Predecir toda la malla
Z = modelo.predict(
    np.c_[xx.ravel(), yy.ravel()]
)

Z = Z.reshape(xx.shape)

# =========================
# Graficar
# =========================

plt.contourf(xx, yy, Z, alpha=0.3)

plt.scatter(
    X[:,0],
    X[:,1],
    c=y
)

# Vectores soporte
plt.scatter(
    modelo.support_vectors_[:,0],
    modelo.support_vectors_[:,1],
    s=100,
    facecolors='none',
    edgecolors='k',
    label="Vectores soporte"
)

plt.title("SVM con Kernel RBF")

plt.legend()

plt.show()