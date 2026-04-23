# Definimos la función de utilidad
def utilidad(dinero):
    # Supongamos una utilidad simple (lineal)
    return dinero


# Calculamos utilidad esperada
def utilidad_esperada(resultados):
    total = 0
    for probabilidad, resultado in resultados:
        total += probabilidad * utilidad(resultado)
    return total


# Acción 1: Apostar
apostar = [
    (0.5, 100),   # 50% ganar 100
    (0.5, -50)    # 50% perder 50
]

# Acción 2: No apostar
no_apostar = [
    (1.0, 20)     # 100% ganar 20
]


# Calcular utilidades esperadas
eu_apostar = utilidad_esperada(apostar)
eu_no_apostar = utilidad_esperada(no_apostar)

print("Utilidad esperada de apostar:", eu_apostar)
print("Utilidad esperada de no apostar:", eu_no_apostar)


# Decisión
if eu_apostar > eu_no_apostar:
    print("Conviene apostar")
else:
    print("Conviene no apostar")