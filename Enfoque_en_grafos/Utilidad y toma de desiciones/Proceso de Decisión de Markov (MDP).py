# Definición del MDP

states = [0, 1, 2]
actions = ["izquierda", "derecha"]
gamma = 0.9

# Función de transición
def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    else:
        return max(s - 1, 0)

# Recompensa
def reward(s, a, s_next):
    if s_next == 2:
        return 10
    return -1


# Política simple (siempre ir a la derecha)
policy = {0: "derecha", 1: "derecha", 2: "derecha"}


# Simulación de un episodio
def simular(policy, pasos=5):
    s = 0  # estado inicial
    total = 0
    
    for t in range(pasos):
        a = policy[s]
        s_next = transition(s, a)
        r = reward(s, a, s_next)
        
        total += (gamma ** t) * r
        s = s_next
    
    return total


# Ejecutar simulación
resultado = simular(policy)
print("Recompensa acumulada:", resultado)