# Probabilidades dadas

P_A = 0.3
P_not_A = 0.7

# P(B|A)
P_B_given_A = 0.6
P_B_given_not_A = 0.2

# P(C|A,B)
P_C_given_A_B = 0.9
P_C_given_A_notB = 0.5
P_C_given_notA_B = 0.7
P_C_given_notA_notB = 0.1

# --- Enumeración ---

# Caso A = True
P_C_and_A = (
    P_A * (
        P_B_given_A * P_C_given_A_B +
        (1 - P_B_given_A) * P_C_given_A_notB
    )
)

# Caso A = False
P_C_and_notA = (
    P_not_A * (
        P_B_given_not_A * P_C_given_notA_B +
        (1 - P_B_given_not_A) * P_C_given_notA_notB
    )
)

# Normalización
P_A_given_C = P_C_and_A / (P_C_and_A + P_C_and_notA)

print("P(A | C) =", P_A_given_C)