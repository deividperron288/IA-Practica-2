import numpy as np

# ==========================================
# CORPUS BILINGÜE
# ==========================================

corpus = [
    ("hola", "hello"),
    ("mundo", "world"),
    ("gato", "cat"),
    ("perro", "dog"),
    ("come", "eats"),
    ("corre", "runs"),
    ("el gato", "the cat"),
    ("el perro", "the dog")
]

# ==========================================
# MODELO DE TRADUCCIÓN
# ==========================================

translation_model = {}

for source, target in corpus:

    source_words = source.split()
    target_words = target.split()

    for s, t in zip(source_words, target_words):

        if s not in translation_model:
            translation_model[s] = {}

        if t not in translation_model[s]:
            translation_model[s][t] = 0

        translation_model[s][t] += 1

# ==========================================
# NORMALIZAR PROBABILIDADES
# ==========================================

for source_word in translation_model:

    total = sum(translation_model[source_word].values())

    for target_word in translation_model[source_word]:

        translation_model[source_word][target_word] /= total

# ==========================================
# MOSTRAR PROBABILIDADES
# ==========================================

print("=== MODELO DE TRADUCCIÓN ===\n")

for source_word in translation_model:

    print(f"{source_word} -> {translation_model[source_word]}")

# ==========================================
# FUNCIÓN DE TRADUCCIÓN
# ==========================================

def translate(sentence):

    words = sentence.split()

    translated_sentence = []

    for word in words:

        if word in translation_model:

            # Obtener traducción más probable
            translations = translation_model[word]

            best_translation = max(
                translations,
                key=translations.get
            )

            translated_sentence.append(best_translation)

        else:
            translated_sentence.append("[UNK]")

    return " ".join(translated_sentence)

# ==========================================
# PRUEBAS
# ==========================================

test_sentences = [
    "hola mundo",
    "el gato come",
    "el perro corre",
    "gato corre"
]

print("\n=== TRADUCCIONES ===\n")

for sentence in test_sentences:

    translated = translate(sentence)

    print(f"{sentence} -> {translated}")