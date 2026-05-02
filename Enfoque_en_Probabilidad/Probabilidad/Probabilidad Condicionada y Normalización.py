import numpy as np

# Ejemplo: datos de personas
# 1 = tiene gripe, 0 = no
gripe = np.array([1, 1, 0, 1, 0, 0, 1, 0])

# 1 = tiene fiebre, 0 = no
fiebre = np.array([1, 1, 1, 0, 0, 0, 1, 0])

# Total de personas con fiebre
total_fiebre = np.sum(fiebre == 1)

# Personas con gripe y fiebre
gripe_y_fiebre = np.sum((gripe == 1) & (fiebre == 1))

# Probabilidad condicionada P(gripe | fiebre)
P_gripe_dado_fiebre = gripe_y_fiebre / total_fiebre

print("P(gripe | fiebre):", P_gripe_dado_fiebre)


# -------------------------
# NORMALIZACIÓN
# -------------------------

valores = np.array([2, 3, 5])

# Normalizar
probabilidades = valores / np.sum(valores)

print("Probabilidades normalizadas:", probabilidades)