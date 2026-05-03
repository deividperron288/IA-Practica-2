import random

# Probabilidades
def sample_A():
    return 1 if random.random() < 0.3 else 0

def P_B_given_A(b, a):
    if a == 1:
        return 0.8 if b == 1 else 0.2
    else:
        return 0.2 if b == 1 else 0.8

# Parámetros
N = 10000
weights_A1 = 0
weights_total = 0

# Evidencia: B = 1
evidence_B = 1

for _ in range(N):
    # 1. Muestrear A
    A = sample_A()

    # 2. NO muestreamos B (está fijado)
    B = evidence_B

    # 3. Calcular peso
    weight = P_B_given_A(B, A)

    # 4. Acumular pesos
    weights_total += weight

    if A == 1:
        weights_A1 += weight

# Estimación
P_A_given_B = weights_A1 / weights_total

print("P(A=1 | B=1) ≈", P_A_given_B)