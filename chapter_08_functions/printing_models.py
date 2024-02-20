import printing_functions as p

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
p.print_models(unprinted_designs, completed_models)
p.show_completed_models(completed_models)
