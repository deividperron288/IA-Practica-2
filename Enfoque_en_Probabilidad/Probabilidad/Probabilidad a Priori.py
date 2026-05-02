import numpy as np

# 1. Datos (1 = spam, 0 = no spam)
datos = np.array([1, 0, 0, 1, 0, 0, 1, 0, 0, 0])

# 2. Calcular probabilidades a priori
total = len(datos)

P_spam = np.sum(datos == 1) / total
P_no_spam = np.sum(datos == 0) / total

print("Probabilidad a priori de spam:", P_spam)
print("Probabilidad a priori de no spam:", P_no_spam)