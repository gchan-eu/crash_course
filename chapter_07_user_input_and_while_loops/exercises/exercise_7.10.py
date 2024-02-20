# Dream Vacation

dream_vacation = []
prompt = "\nIf you could visit one place in the world, where would you go? "
polling_active = True
while polling_active:
    place = input(prompt)
    dream_vacation.append(place)
    repeat = input("Continue poll (y/n)? ")
    polling_active = (repeat == 'y')

for place in set(dream_vacation):
    print(place.title())

