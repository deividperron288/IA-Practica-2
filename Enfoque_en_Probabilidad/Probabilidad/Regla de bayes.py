import numpy as np

# 1. Probabilidad a priori
P_enfermedad = 0.01  # 1%

# 2. Probabilidad del test
P_positivo_dado_enfermedad = 0.95  # sensibilidad
P_positivo_dado_no_enfermedad = 0.05  # falso positivo

# 3. Probabilidad total de positivo
P_positivo = (P_positivo_dado_enfermedad * P_enfermedad +
              P_positivo_dado_no_enfermedad * (1 - P_enfermedad))

# 4. Aplicar Bayes
P_enfermedad_dado_positivo = (P_positivo_dado_enfermedad * P_enfermedad) / P_positivo

print("Probabilidad de tener la enfermedad dado positivo:",
      P_enfermedad_dado_positivo)