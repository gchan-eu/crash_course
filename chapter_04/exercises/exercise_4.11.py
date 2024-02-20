# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# Make a copy of the list of pizzas, and call it friend_pizzas.

my_pizzas = ['Tropicana', "Mama's Pizza", 'Ham & Bacon Classic', 'Bourbon']

friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list.

my_pizzas.append('Special')

# Add a different pizza to the list friend_pizzas.

friend_pizzas.append('Four Seasons')

# Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

