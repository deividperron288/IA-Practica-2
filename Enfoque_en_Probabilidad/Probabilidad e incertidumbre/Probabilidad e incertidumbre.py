import numpy as np

# Probabilidad de tener la enfermedad (prior)
P_enfermedad = 0.01  # 1%

# Probabilidad de dar positivo si tienes la enfermedad (sensibilidad)
P_positivo_dado_enfermedad = 0.95

# Probabilidad de dar positivo sin tener la enfermedad (falso positivo)
P_positivo_dado_no_enfermedad = 0.05

# Probabilidad total de dar positivo
P_positivo = (P_positivo_dado_enfermedad * P_enfermedad +
              P_positivo_dado_no_enfermedad * (1 - P_enfermedad))

# Aplicando Teorema de Bayes
P_enfermedad_dado_positivo = (P_positivo_dado_enfermedad * P_enfermedad) / P_positivo

print("Probabilidad de tener la enfermedad dado positivo:", P_enfermedad_dado_positivo)