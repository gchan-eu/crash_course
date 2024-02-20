wife = {
    'first_name': 'michelle',
    'last_name': 'lowry',
    'age': 46, 
    'city': 'agios konstantinos'
    }

son = {
    'first_name': 'chris',
    'last_name': 'chantzopoulos',
    'age': 30, 
    'city': 'thun'
    }

daughter = {
    'first_name': 'luita',
    'last_name': 'chantzopoulos',
    'age': 26, 
    'city': 'cologne'
    }

favorite_people = [wife, son, daughter]

for person in favorite_people:
    print("Full Name is " + 
        person['first_name'].title() + " " + 
        person['last_name'].title())
    print("Age is " + str(person['age']))
    print("City is " + person['city'].title())

    