# Probabilidades iniciales
prob_clima = {
    "lluvia": 0.3,
    "no_lluvia": 0.7
}

# Función de utilidad
def utilidad(decision, clima):
    if decision == "paraguas":
        return 10 if clima == "lluvia" else -5
    else:  # no_paraguas
        return -20 if clima == "lluvia" else 15


# Utilidad esperada SIN información
def utilidad_esperada_sin_info():
    decisiones = ["paraguas", "no_paraguas"]
    
    def EU(d):
        return sum(prob_clima[c] * utilidad(d, c) for c in prob_clima)
    
    return max(EU(d) for d in decisiones)


# Utilidad esperada CON información perfecta
def utilidad_esperada_con_info():
    total = 0
    
    for clima, prob in prob_clima.items():
        # Elegimos la mejor decisión sabiendo el clima
        decisiones = ["paraguas", "no_paraguas"]
        mejor_utilidad = max(utilidad(d, clima) for d in decisiones)
        
        total += prob * mejor_utilidad
    
    return total


# Calcular VOI
eu_sin = utilidad_esperada_sin_info()
eu_con = utilidad_esperada_con_info()

voi = eu_con - eu_sin

print("EU sin información:", eu_sin)
print("EU con información:", eu_con)
print("Valor de la información:", voi)