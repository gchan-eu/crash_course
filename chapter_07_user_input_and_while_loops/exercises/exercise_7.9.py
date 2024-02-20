sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'club', 'turkey', 'pastrami', 'blt']
finished_sandwiches = []

print("\nDeli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nPending orders:")
for sandwich in sandwich_orders:
    print("\tPending order for a " + sandwich + " sandwich.")