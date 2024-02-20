prompt = "\nPlease enter a pizza topping."
prompt += "\nEnter 'quit' to exit: "

while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    print(pizza_topping.title() + " has beed added to your pizza.")

