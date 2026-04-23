# Probabilidades del nodo de azar (clima)
prob_clima = {
    "lluvia": 0.3,
    "no_lluvia": 0.7
}


# Función de utilidad
def utilidad(decision, clima):
    if decision == "paraguas":
        if clima == "lluvia":
            return 10
        else:
            return -5
    else:  # no_paraguas
        if clima == "lluvia":
            return -20
        else:
            return 15


# Calcular utilidad esperada
def utilidad_esperada(decision):
    total = 0
    for clima, prob in prob_clima.items():
        total += prob * utilidad(decision, clima)
    return total


# Evaluar decisiones
decisiones = ["paraguas", "no_paraguas"]

for d in decisiones:
    print(f"Utilidad esperada de {d}: {utilidad_esperada(d)}")


# Elegir mejor decisión
mejor = max(decisiones, key=utilidad_esperada)
print("\nMejor decisión:", mejor)