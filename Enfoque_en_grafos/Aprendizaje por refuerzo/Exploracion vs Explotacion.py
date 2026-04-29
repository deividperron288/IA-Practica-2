import random

# Acciones
actions = ["A", "B"]

# Recompensas reales (desconocidas para el agente)
true_rewards = {
    "A": 5,
    "B": 10
}

# Estimaciones iniciales
Q = {a: 0 for a in actions}
N = {a: 0 for a in actions}

epsilon = 0.2  # probabilidad de explorar


def elegir_accion():
    if random.random() < epsilon:
        return random.choice(actions)  # explorar
    return max(actions, key=lambda a: Q[a])  # explotar


# Simulación
for _ in range(100):
    a = elegir_accion()
    
    # Simular recompensa con ruido
    r = true_rewards[a] + random.randint(-2, 2)
    
    # Actualizar promedio
    N[a] += 1
    Q[a] += (r - Q[a]) / N[a]


print("Estimaciones Q:", Q)
print("Veces elegidas:", N)
print("Mejor acción aprendida:", max(Q, key=Q.get))