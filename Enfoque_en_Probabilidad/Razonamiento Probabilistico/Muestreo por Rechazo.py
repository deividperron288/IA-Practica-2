import random

def sample_A():
    return 1 if random.random() < 0.3 else 0

def sample_B(a):
    if a == 1:
        return 1 if random.random() < 0.8 else 0
    return 1 if random.random() < 0.2 else 0


samples = 10000
accepted = 0
count_A1 = 0

for _ in range(samples):
    A = sample_A()
    B = sample_B(A)

    # Evidencia: B = 1
    if B == 1:
        accepted += 1

        if A == 1:
            count_A1 += 1

# Aproximación de P(A=1 | B=1)
resultado = count_A1 / accepted

print("P(A=1 | B=1) ≈", resultado)
print("Muestras aceptadas:", accepted)