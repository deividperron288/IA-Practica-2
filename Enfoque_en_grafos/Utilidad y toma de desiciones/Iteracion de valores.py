# Estados
states = [0, 1, 2]

# Acciones posibles
actions = ["izquierda", "derecha"]

# Factor de descuento
gamma = 0.9

# Recompensas
def reward(s, a, s_next):
    if s_next == 2:
        return 10
    return -1

# Transiciones (deterministas)
def transition(s, a):
    if a == "derecha":
        return min(s + 1, 2)
    else:
        return max(s - 1, 0)

# Inicializar valores
V = {s: 0 for s in states}

# Iteración de valores
for _ in range(10):  # número de iteraciones
    new_V = V.copy()
    
    for s in states:
        valores_acciones = []
        
        for a in actions:
            s_next = transition(s, a)
            r = reward(s, a, s_next)
            
            valor = r + gamma * V[s_next]
            valores_acciones.append(valor)
        
        new_V[s] = max(valores_acciones)
    
    V = new_V

print("Valores finales:", V)


# Derivar política óptima
policy = {}

for s in states:
    mejor_accion = None
    mejor_valor = float("-inf")
    
    for a in actions:
        s_next = transition(s, a)
        r = reward(s, a, s_next)
        
        valor = r + gamma * V[s_next]
        
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_accion = a
    
    policy[s] = mejor_accion

print("Política óptima:", policy)