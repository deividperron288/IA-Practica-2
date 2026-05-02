import numpy as np

np.random.seed(0)
n = 1000

# Variable C (lluvia)
C = np.random.choice([0, 1], size=n)  # 0=no, 1=sí

# A depende SOLO de C
A = np.where(C == 1,
             np.random.choice([0, 1], size=n, p=[0.2, 0.8]),
             np.random.choice([0, 1], size=n, p=[0.7, 0.3]))

# B también depende SOLO de C
B = np.where(C == 1,
             np.random.choice([0, 1], size=n, p=[0.3, 0.7]),
             np.random.choice([0, 1], size=n, p=[0.8, 0.2]))

# -------------------------
# Calcular probabilidades
# -------------------------

# P(A=1 | C=1)
P_A_dado_C = np.sum((A == 1) & (C == 1)) / np.sum(C == 1)

# P(A=1 | B=1, C=1)
P_A_dado_BC = np.sum((A == 1) & (B == 1) & (C == 1)) / np.sum((B == 1) & (C == 1))

print("P(A=1 | C=1):", P_A_dado_C)
print("P(A=1 | B=1, C=1):", P_A_dado_BC)