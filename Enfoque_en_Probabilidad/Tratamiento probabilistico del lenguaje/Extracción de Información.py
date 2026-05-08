import re
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. TEXTO DE ENTRADA
# ==========================================

texto = """
Juan trabaja en Google desde 2020.
Maria estudia en la Universidad Nacional.
Pedro fue contratado por Microsoft en 2023.
"""

print("TEXTO ORIGINAL:\n")
print(texto)

# ==========================================
# 2. PATRONES DE EXTRACCIÓN
# ==========================================

# Personas (palabras con mayúscula inicial)
patron_personas = r"\b[A-Z][a-z]+\b"

# Fechas
patron_fechas = r"\b\d{4}\b"

# Organizaciones
organizaciones_conocidas = [
    "Google",
    "Microsoft",
    "Universidad Nacional"
]

# ==========================================
# 3. EXTRAER PERSONAS
# ==========================================

personas = re.findall(patron_personas, texto)

# ==========================================
# 4. EXTRAER FECHAS
# ==========================================

fechas = re.findall(patron_fechas, texto)

# ==========================================
# 5. EXTRAER ORGANIZACIONES
# ==========================================

organizaciones = []

for org in organizaciones_conocidas:
    
    if org in texto:
        organizaciones.append(org)

# ==========================================
# 6. MOSTRAR RESULTADOS
# ==========================================

print("\nPERSONAS ENCONTRADAS:")
print(personas)

print("\nFECHAS ENCONTRADAS:")
print(fechas)

print("\nORGANIZACIONES ENCONTRADAS:")
print(organizaciones)

# ==========================================
# 7. SIMULAR PROBABILIDADES
# ==========================================

# Probabilidades simuladas de confianza

confianza = {
    
    "Personas": 0.90,
    "Fechas": 0.95,
    "Organizaciones": 0.85
}

print("\nNIVELES DE CONFIANZA:\n")

for categoria, prob in confianza.items():
    
    print(f"{categoria}: {prob}")

# ==========================================
# 8. VISUALIZACIÓN
# ==========================================

categorias = list(confianza.keys())
valores = list(confianza.values())

plt.figure(figsize=(8,5))

plt.bar(categorias, valores)

plt.ylim(0,1)

plt.ylabel("Probabilidad")
plt.title("Confianza de extracción")

plt.show()