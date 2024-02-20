favorite_numbers = {
    'michelle': 22, 
    'lucas': 7, 
    'chris': 13, 
    'luita': 6, 
    'sierra': 16
    }

print("Michelle " + str(favorite_numbers['michelle']))
print("Lucas " + str(favorite_numbers['lucas']))
print("Chris " + str(favorite_numbers['chris']))
print("Luita " + str(favorite_numbers['luita']))
print("Sierra " + str(favorite_numbers['sierra']))

print("\n")

for person in favorite_numbers:
    print(person.title(), favorite_numbers[person])

