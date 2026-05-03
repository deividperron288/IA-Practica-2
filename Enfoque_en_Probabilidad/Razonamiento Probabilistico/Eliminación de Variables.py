# Supongamos factores simples

# Factor 1: P(A)
P_A = [0.7, 0.3]

# Factor 2: P(B|A)
P_B_given_A = [
    [0.6, 0.4],  # B=0 dado A=0, A=1
    [0.4, 0.6]
]

# Eliminación de B (sumar sobre B)
factor_reducido = []

for a in range(2):
    suma = 0
    for b in range(2):
        suma += P_B_given_A[b][a]
    factor_reducido.append(suma)

print("Factor después de eliminar B:", factor_reducido)