favorite_places = {}

favorite_places['georgios'] = ['nile river', 'santorini', 'niagara falls']
favorite_places['michelle'] = ['antarctica', 'mykonos']
favorite_places['soula'] = ['voutoumi']

for name, places in favorite_places.items():
    print(name)
    for place in places:
        print("\t" + place)
