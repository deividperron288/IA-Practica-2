# Estados
states = [0, 1, 2]

# Acciones
actions = ["izquierda", "derecha"]

# Factor de descuento
gamma = 0.9

# Recompensa
def reward(s, a, s_next):
    if s_next == 2:
        return 10
    return -1

# Transición determinista
def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    else:
        return max(s - 1, 0)


# Inicializar política arbitraria
policy = {s: "izquierda" for s in states}

# Inicializar valores
V = {s: 0 for s in states}


def evaluar_politica(policy, V, iteraciones=10):
    for _ in range(iteraciones):
        for s in states:
            a = policy[s]
            s_next = transition(s, a)
            V[s] = reward(s, a, s_next) + gamma * V[s_next]
    return V


def mejorar_politica(policy, V):
    estable = True
    
    for s in states:
        mejor_accion = None
        mejor_valor = float("-inf")
        
        for a in actions:
            s_next = transition(s, a)
            valor = reward(s, a, s_next) + gamma * V[s_next]
            
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = a
        
        if mejor_accion != policy[s]:
            estable = False
        
        policy[s] = mejor_accion
    
    return policy, estable


# Iteración de políticas
while True:
    V = evaluar_politica(policy, V)
    policy, estable = mejorar_politica(policy, V)
    
    if estable:
        break


print("Valores finales:", V)
print("Política óptima:", policy)