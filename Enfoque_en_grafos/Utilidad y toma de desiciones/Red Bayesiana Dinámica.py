import random

# Estados posibles
states = ["lluvia", "no_lluvia"]

# Probabilidades de transición P(s_t+1 | s_t)
transition_model = {
    "lluvia": {
        "lluvia": 0.7,
        "no_lluvia": 0.3
    },
    "no_lluvia": {
        "lluvia": 0.2,
        "no_lluvia": 0.8
    }
}

# Modelo de observación P(obs | estado)
observation_model = {
    "lluvia": {
        "paraguas": 0.9,
        "no_paraguas": 0.1
    },
    "no_lluvia": {
        "paraguas": 0.2,
        "no_paraguas": 0.8
    }
}


# Función para muestrear probabilidades
def sample(prob_dict):
    r = random.random()
    acumulado = 0
    
    for estado, prob in prob_dict.items():
        acumulado += prob
        if r <= acumulado:
            return estado


# Simulación de la DBN
def simular(pasos=5):
    estado_actual = "no_lluvia"
    
    for t in range(pasos):
        # Generar observación
        observacion = sample(observation_model[estado_actual])
        
        print(f"Tiempo {t}: Estado real = {estado_actual}, Observación = {observacion}")
        
        # Transición al siguiente estado
        estado_actual = sample(transition_model[estado_actual])


# Ejecutar simulación
simular()