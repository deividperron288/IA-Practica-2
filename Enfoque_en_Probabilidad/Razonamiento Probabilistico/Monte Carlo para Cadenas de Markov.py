import random

# Probabilidades condicionales
def sample_A_given_B(b):
    if b == 1:
        return 1 if random.random() < 0.7 else 0
    else:
        return 1 if random.random() < 0.2 else 0

def sample_B_given_A(a):
    if a == 1:
        return 1 if random.random() < 0.8 else 0
    else:
        return 1 if random.random() < 0.3 else 0

# Inicialización
A = 0
B = 0

samples = []

# Iteraciones MCMC
for _ in range(10000):
    # Paso 1: muestrear A dado B
    A = sample_A_given_B(B)

    # Paso 2: muestrear B dado A
    B = sample_B_given_A(A)

    samples.append((A, B))

# Estimar P(A=1)
count_A1 = sum(1 for s in samples if s[0] == 1)

print("P(A=1) ≈", count_A1 / len(samples))