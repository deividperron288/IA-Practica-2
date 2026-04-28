# Estrategias
strategies = ["cooperar", "traicionar"]

# Matriz de pagos (jugador1, jugador2)
payoff = {
    ("cooperar", "cooperar"): (3, 3),
    ("cooperar", "traicionar"): (0, 5),
    ("traicionar", "cooperar"): (5, 0),
    ("traicionar", "traicionar"): (1, 1),
}


# Verificar si es equilibrio de Nash
def es_nash(s1, s2):
    p1, p2 = payoff[(s1, s2)]
    
    # Jugador 1 intenta cambiar
    for alt1 in strategies:
        if payoff[(alt1, s2)][0] > p1:
            return False
    
    # Jugador 2 intenta cambiar
    for alt2 in strategies:
        if payoff[(s1, alt2)][1] > p2:
            return False
    
    return True


# Buscar equilibrios
equilibrios = []

for s1 in strategies:
    for s2 in strategies:
        if es_nash(s1, s2):
            equilibrios.append((s1, s2))

print("Equilibrios de Nash:", equilibrios)