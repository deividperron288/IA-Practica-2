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


# Generar política aleatoria (probabilidad de ir derecha)
def generar_politica():
    return {s: random.random() for s in states}


# Ejecutar episodio
def evaluar_politica(policy, episodios=10):
    total = 0
    
    for _ in range(episodios):
        s = 0
        G = 0
        t = 0
        
        while s != 2:
            # decisión probabilística
            if random.random() < policy[s]:
                a = "derecha"
            else:
                a = "izquierda"
            
            s_next = transition(s, a)
            r = reward(s, s_next)
            
            G += (gamma ** t) * r
            s = s_next
            t += 1
        
        total += G
    
    return total / episodios


# Búsqueda de política
mejor_politica = None
mejor_valor = float("-inf")

for _ in range(50):  # probar 50 políticas
    politica = generar_politica()
    valor = evaluar_politica(politica)
    
    if valor > mejor_valor:
        mejor_valor = valor
        mejor_politica = politica


print("Mejor política encontrada:", mejor_politica)
print("Valor:", mejor_valor)