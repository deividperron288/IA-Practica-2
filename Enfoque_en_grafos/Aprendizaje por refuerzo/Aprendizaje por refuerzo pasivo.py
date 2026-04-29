import random

# Estados
states = [0, 1, 2]

# Política fija
policy = {
    0: "derecha",
    1: "derecha",
    2: "derecha"
}

gamma = 0.9
alpha = 0.1  # tasa de aprendizaje

# Transición
def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    return max(s - 1, 0)

# Recompensa
def reward(s, s_next):
    if s_next == 2:
        return 10
    return -1

# Inicializar valores
V = {s: 0 for s in states}


# Episodio de entrenamiento
def episodio():
    s = 0
    
    while s != 2:  # hasta llegar a meta
        a = policy[s]
        s_next = transition(s, a)
        r = reward(s, s_next)
        
        # TD(0)
        V[s] = V[s] + alpha * (r + gamma * V[s_next] - V[s])
        
        s = s_next


# Entrenar
for _ in range(100):
    episodio()

print("Valores aprendidos:", V)