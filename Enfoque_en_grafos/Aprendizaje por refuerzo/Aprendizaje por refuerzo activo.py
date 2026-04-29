import random

states = [0, 1, 2]
actions = ["izquierda", "derecha"]

gamma = 0.9

# Transición
def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    return max(s - 1, 0)

# Recompensa
def reward(s, s_next):
    return 10 if s_next == 2 else -1


# Guardamos recompensas acumuladas
returns = {(s, a): [] for s in states for a in actions}
Q = {(s, a): 0 for s in states for a in actions}


def generar_episodio():
    s = 0
    episodio = []
    
    while s != 2:
        a = random.choice(actions)  # exploración total
        s_next = transition(s, a)
        r = reward(s, s_next)
        
        episodio.append((s, a, r))
        s = s_next
    
    return episodio


# Entrenamiento Monte Carlo
for _ in range(100):
    episodio = generar_episodio()
    G = 0
    
    for s, a, r in reversed(episodio):
        G = gamma * G + r
        returns[(s, a)].append(G)
        Q[(s, a)] = sum(returns[(s, a)]) / len(returns[(s, a)])


# Política
policy = {s: max(actions, key=lambda a: Q[(s, a)]) for s in states}

print("Q:", Q)
print("Política:", policy)