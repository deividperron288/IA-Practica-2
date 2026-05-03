import numpy as np

# Probabilidades
P_A = 0.3

# P(B|A) y P(B|¬A)
P_B_given_A = np.array([0.4, 0.6])   # [P(B=0|A), P(B=1|A)]

# P(C|A,B)
# filas: B, columnas: A
P_C_given_AB = np.array([
    [0.2, 0.3],  # B=0
    [0.7, 0.9]   # B=1
])

# Elegimos valores específicos
A = 1
B = 1
C = 1

# Aplicar regla de la cadena
P_ABC = P_A * P_B_given_A[B] * P_C_given_AB[B][A]

print("P(A=1, B=1, C=1) =", P_ABC)