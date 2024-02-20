prompt = "\nPlease enter your age."
prompt += "\nEnter 'quit' to exit: "

active = True
while active:
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15
        print("The cost for your ticket is " + str(price) + ".")
    else:
        active = False


