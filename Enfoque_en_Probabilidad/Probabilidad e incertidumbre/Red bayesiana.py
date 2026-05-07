import numpy as np
import matplotlib.pyplot as plt

# =========================================
# RED BAYESIANA SIMPLE
#
# Lluvia ----\
#              ---> Pasto Mojado
# Aspersor --/
# =========================================


# =========================================
# 1. Probabilidades iniciales
# =========================================

# P(Lluvia)
# [No lluvia, Lluvia]
P_lluvia = np.array([0.8, 0.2])

# P(Aspersor)
# [No aspersor, Aspersor]
P_aspersor = np.array([0.7, 0.3])


# =========================================
# 2. Probabilidad condicional
# P(PastoMojado | Lluvia, Aspersor)
# =========================================

# Estructura:
#
# P_pasto[Lluvia][Aspersor][Pasto]
#
# Pasto:
# 0 = No mojado
# 1 = Mojado

P_pasto = np.array([

    # Lluvia = 0 (No lluvia)
    [
        [0.9, 0.1],   # Aspersor = 0
        [0.4, 0.6]    # Aspersor = 1
    ],

    # Lluvia = 1 (Lluvia)
    [
        [0.3, 0.7],   # Aspersor = 0
        [0.1, 0.9]    # Aspersor = 1
    ]

])


# =========================================
# 3. Calcular:
# P(Lluvia | Pasto Mojado)
# =========================================

# =========================================
# Numerador:
# P(Lluvia y Pasto Mojado)
# =========================================

P_L_y_M = 0

for aspersor in [0, 1]:

    # P(Lluvia)
    P_L = P_lluvia[1]

    # P(Aspersor)
    P_A = P_aspersor[aspersor]

    # P(Pasto mojado | Lluvia, Aspersor)
    P_M_dado = P_pasto[1][aspersor][1]

    # Multiplicación conjunta
    P_L_y_M += P_L * P_A * P_M_dado


# =========================================
# Denominador:
# P(Pasto Mojado)
# =========================================

P_M = 0

for lluvia in [0, 1]:
    for aspersor in [0, 1]:

        P_L = P_lluvia[lluvia]

        P_A = P_aspersor[aspersor]

        P_M_dado = P_pasto[lluvia][aspersor][1]

        P_M += P_L * P_A * P_M_dado


# =========================================
# Aplicar Regla de Bayes
# =========================================

P_L_dado_M = P_L_y_M / P_M


# =========================================
# Mostrar resultados
# =========================================

print("=================================")
print("RESULTADOS")
print("=================================")

print(f"P(Pasto Mojado) = {P_M:.4f}")

print(f"P(Lluvia y Pasto Mojado) = {P_L_y_M:.4f}")

print(f"P(Lluvia | Pasto Mojado) = {P_L_dado_M:.4f}")

print("=================================")


# =========================================
# 4. Graficar resultados
# =========================================

labels = ['No Lluvia', 'Lluvia']

valores = [
    1 - P_L_dado_M,
    P_L_dado_M
]

plt.figure(figsize=(6, 4))

plt.bar(labels, valores)

plt.title('Probabilidad de Lluvia dado Pasto Mojado')

plt.ylabel('Probabilidad')

plt.ylim(0, 1)

# Mostrar valores encima de las barras
for i, v in enumerate(valores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center')

plt.show()