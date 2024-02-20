# Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

menu = ('Grilled Salmon', 'Pork Steak', 'Mushroom Soup', 'Chef Salad', "Ceasar's Salad")

# Use a for loop to print each food the restaurant offers.

for food in menu:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
    
#menu[1] = 'Cod'
    
# The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

menu = ('Grilled Salmon', 'Chicago Burger', 'Mushroom Soup', 'Chef Salad', 'Fish Fillet')
for food in menu:
    print(food)
