sandwich_orders = ['grilled cheese', 'turkey', 'tuna', 'club', 'turkey', 'grilled cheese', 'blt']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Processing a " + sandwich + " sandwich order.")
    finished_sandwiches.append(sandwich)

print("\nCompleted orders:")
for finished_sandwich in finished_sandwiches:
    print("\tCompleted order for a " + finished_sandwich + " sandwich.")