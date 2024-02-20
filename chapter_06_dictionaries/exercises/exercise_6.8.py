# Pet dictionaries

max = {'animal': 'cat', 'owner': 'michelle'}
elsa = {'animal': 'dog', 'owner': 'luita'}
derek = {'animal': 'dog', 'owner': 'sarah'}
martin = {'animal': 'dog', 'owner': 'sarah'}
hit = {'animal': 'cat', 'owner': 'michelle'}

pets = [max, elsa, derek, martin, hit]

for pet in pets:
    print(pet['animal'], pet['owner'])