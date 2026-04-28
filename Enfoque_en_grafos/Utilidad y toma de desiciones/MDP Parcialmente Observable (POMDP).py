# Estados posibles
states = ["lluvia", "no_lluvia"]

# Creencia inicial (probabilidad)
belief = {
    "lluvia": 0.3,
    "no_lluvia": 0.7
}

# Modelo de observación P(obs | estado)
# Ejemplo: sensor de suelo mojado
observation_model = {
    "mojado": {
        "lluvia": 0.8,
        "no_lluvia": 0.2
    },
    "seco": {
        "lluvia": 0.2,
        "no_lluvia": 0.8
    }
}


# Actualización de creencia (Bayes)
def actualizar_belief(belief, observacion):
    nuevo_belief = {}
    total = 0

    for s in states:
        prob = observation_model[observacion][s] * belief[s]
        nuevo_belief[s] = prob
        total += prob

    # Normalizar
    for s in states:
        nuevo_belief[s] /= total

    return nuevo_belief


# Simulación de observación
observacion = "mojado"

nuevo_belief = actualizar_belief(belief, observacion)

print("Creencia antes:", belief)
print("Observación:", observacion)
print("Creencia después:", nuevo_belief)