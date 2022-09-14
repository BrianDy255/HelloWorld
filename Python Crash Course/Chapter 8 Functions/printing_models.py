def print_models(unprinted_designs,completed_designs):
    """Function to pop and append a llist"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Currently printing out: {current_design.title()}')
        completed_designs.append(current_design)

def show_completed_models(completed_designs):
    for complete in completed_designs:
        print(f'The following models have been completed: {complete.title()}')

unprinted_designs = ['iPhone case', 'dog bowl', 'dodecahedron']
completed_designs = []

print_models(unprinted_designs[:],completed_designs)
show_completed_models(completed_designs)