import random

states = [0, 1, 2]
actions = ["izquierda", "derecha"]

gamma = 0.9
alpha = 0.1
epsilon = 0.2

def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    return max(s - 1, 0)

def reward(s, s_next):
    return 10 if s_next == 2 else -1

Q = {(s, a): 0 for s in states for a in actions}


def elegir_accion(s):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(actions, key=lambda a: Q[(s, a)])


# Entrenamiento
for _ in range(100):
    s = 0
    
    while s != 2:
        a = elegir_accion(s)
        s_next = transition(s, a)
        r = reward(s, s_next)
        
        max_q = max(Q[(s_next, a2)] for a2 in actions)
        Q[(s, a)] += alpha * (r + gamma * max_q - Q[(s, a)])
        
        s = s_next


policy = {s: max(actions, key=lambda a: Q[(s, a)]) for s in states}

print("Q:", Q)
print("Política:", policy)