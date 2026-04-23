from itertools import product

# Variables y dominios
variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Restricciones
def constraints(assignment):
    if 'A' in assignment and 'B' in assignment:
        if assignment['A'] == assignment['B']:
            return False
    if 'B' in assignment and 'C' in assignment:
        if assignment['B'] == assignment['C']:
            return False
    if 'C' in assignment and 'A' in assignment:
        if assignment['C'] == assignment['A']:
            return False
    return True


# Resolver árbol (B y C)
def solve_tree(assignment):
    solutions = []
    for b, c in product(domains['B'], domains['C']):
        assignment_temp = assignment.copy()
        assignment_temp['B'] = b
        assignment_temp['C'] = c
        
        if constraints(assignment_temp):
            solutions.append(assignment_temp)
    
    return solutions


# Cutset Conditioning
def cutset_conditioning():
    solutions = []
    
    # Cutset = ['A']
    for a in domains['A']:
        assignment = {'A': a}
        
        if not constraints(assignment):
            continue
        
        # Resolver el resto (árbol)
        tree_solutions = solve_tree(assignment)
        solutions.extend(tree_solutions)
    
    return solutions


# Ejecutar
result = cutset_conditioning()

for sol in result:
    print(sol)