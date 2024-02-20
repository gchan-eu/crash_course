favorite_numbers = {
    'michelle': [22, 15], 
    'lucas': [7], 
    'chris': [13, 56, 3], 
    'luita': [6], 
    'sierra': [16, 0],
    }

for person, numbers in favorite_numbers.items():
    print(person.title())
    for number in numbers:
        print("\t" + str(number))