from itertools import product

def eval_formula(model):
    # model: dictionary {'A': True, 'B': False}
    A = model['A']
    B = model['B']
    return (A or B) and (not A or B)

# Semua kemungkinan nilai A, B
variables = ['A', 'B']
models = list(product([False, True], repeat=len(variables)))

print("Hasil model checking:")
for assignment in models:
    model = dict(zip(variables, assignment))
    result = eval_formula(model)
    print(f"Model: {model}, Formula terpenuhi? {result}")