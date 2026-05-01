from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Definir la estructura de la red
model = BayesianNetwork([
    ('Lluvia', 'PastoMojado'),
    ('Aspersor', 'PastoMojado')
])

# 2. Definir probabilidades

# Probabilidad de lluvia
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2,
                        values=[[0.8], [0.2]])  # No lluvia, Lluvia

# Probabilidad de aspersor
cpd_aspersor = TabularCPD(variable='Aspersor', variable_card=2,
                          values=[[0.7], [0.3]])

# Probabilidad de pasto mojado dependiendo de lluvia y aspersor
cpd_pasto = TabularCPD(variable='PastoMojado', variable_card=2,
                       values=[
                           [0.9, 0.4, 0.3, 0.1],  # No mojado
                           [0.1, 0.6, 0.7, 0.9]   # Mojado
                       ],
                       evidence=['Lluvia', 'Aspersor'],
                       evidence_card=[2, 2])

# 3. Agregar CPDs al modelo
model.add_cpds(cpd_lluvia, cpd_aspersor, cpd_pasto)

# 4. Verificar el modelo
print("¿Modelo válido?", model.check_model())

# 5. Inferencia
inference = VariableElimination(model)

# ¿Probabilidad de lluvia dado que el pasto está mojado?
resultado = inference.query(variables=['Lluvia'], evidence={'PastoMojado': 1})

print(resultado)