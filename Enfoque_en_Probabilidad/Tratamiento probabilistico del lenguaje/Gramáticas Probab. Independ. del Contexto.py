import numpy as np

# ==========================================
# 1. DEFINIR LA GRAMÁTICA PROBABILÍSTICA
# ==========================================

gramatica = {

    "S": [
        (["NP", "VP"], 1.0)
    ],

    "NP": [
        (["Det", "N"], 0.7),
        (["Nombre"], 0.3)
    ],

    "VP": [
        (["V", "NP"], 0.8),
        (["V"], 0.2)
    ],

    "Det": [
        (["el"], 0.5),
        (["la"], 0.5)
    ],

    "N": [
        (["gato"], 0.4),
        (["pescado"], 0.6)
    ],

    "V": [
        (["come"], 1.0)
    ],

    "Nombre": [
        (["juan"], 1.0)
    ]
}

# ==========================================
# 2. FUNCIÓN PARA MOSTRAR REGLAS
# ==========================================

print("GRAMÁTICA:\n")

for no_terminal, reglas in gramatica.items():

    for regla, prob in reglas:

        print(f"{no_terminal} -> {' '.join(regla)}   P={prob}")

# ==========================================
# 3. ORACIÓN DE PRUEBA
# ==========================================

oracion = ["el", "gato", "come", "el", "pescado"]

print("\nOración:")
print(" ".join(oracion))

# ==========================================
# 4. DERIVACIÓN MANUAL
# ==========================================

"""
S
-> NP VP

NP -> Det N
VP -> V NP

Det -> el
N -> gato

V -> come

NP -> Det N
Det -> el
N -> pescado
"""

# ==========================================
# 5. CALCULAR PROBABILIDAD
# ==========================================

probabilidad = (
    
    1.0 *   # S -> NP VP
    
    0.7 *   # NP -> Det N
    
    0.8 *   # VP -> V NP
    
    0.5 *   # Det -> el
    
    0.4 *   # N -> gato
    
    1.0 *   # V -> come
    
    0.7 *   # NP -> Det N
    
    0.5 *   # Det -> el
    
    0.6     # N -> pescado
)

print("\nProbabilidad total:")
print(probabilidad)

# ==========================================
# 6. MOSTRAR EN PORCENTAJE
# ==========================================

print(f"\nProbabilidad porcentual: {probabilidad*100:.2f}%")