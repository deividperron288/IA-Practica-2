import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. DOCUMENTOS
# ==========================================

documentos = [

    "La inteligencia artificial aprende patrones",
    
    "El aprendizaje automatico usa datos",
    
    "Los gatos comen pescado",
    
    "La inteligencia artificial procesa lenguaje natural",
    
    "Los perros juegan en el parque"
]

# ==========================================
# 2. CREAR MODELO TF-IDF
# ==========================================

vectorizador = TfidfVectorizer()

# Convertir documentos a matriz numérica
matriz_tfidf = vectorizador.fit_transform(documentos)

# ==========================================
# 3. MOSTRAR VOCABULARIO
# ==========================================

print("VOCABULARIO:\n")

print(vectorizador.get_feature_names_out())

# ==========================================
# 4. CONSULTA DEL USUARIO
# ==========================================

consulta = ["inteligencia artificial"]

# Convertir consulta a vector
vector_consulta = vectorizador.transform(consulta)

# ==========================================
# 5. CALCULAR SIMILITUD
# ==========================================

similitudes = cosine_similarity(
    
    vector_consulta,
    matriz_tfidf
)

# ==========================================
# 6. MOSTRAR RESULTADOS
# ==========================================

print("\nRESULTADOS:\n")

for i, similitud in enumerate(similitudes[0]):

    print(f"Documento {i+1}")
    print(documentos[i])
    print(f"Similitud: {similitud:.4f}\n")

# ==========================================
# 7. DOCUMENTO MÁS RELEVANTE
# ==========================================

indice_mejor = np.argmax(similitudes)

print("DOCUMENTO MÁS RELEVANTE:\n")

print(documentos[indice_mejor])

# ==========================================
# 8. VISUALIZACIÓN
# ==========================================

plt.figure(figsize=(10,5))

plt.bar(
    range(len(documentos)),
    similitudes[0]
)

plt.xticks(
    range(len(documentos)),
    [f"Doc {i+1}" for i in range(len(documentos))]
)

plt.ylabel("Similitud")
plt.xlabel("Documentos")
plt.title("Similitud entre consulta y documentos")

plt.show()