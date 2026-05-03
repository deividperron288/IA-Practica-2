import random

def sample_A():
    return 1 if random.random() < 0.3 else 0

def sample_B(a):
    if a == 1:
        return 1 if random.random() < 0.8 else 0
    else:
        return 1 if random.random() < 0.2 else 0

# Generar una muestra
A = sample_A()
B = sample_B(A)

print("Muestra generada:")
print("A =", A)
print("B =", B)