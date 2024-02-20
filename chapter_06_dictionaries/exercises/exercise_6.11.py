paris = {
    'country': 'france', 
    'population': 2.161,
    'fact': 'Roman ruins still exist in Paris.',
    }

tokyo = {
    'country': 'japan', 
    'population': 13.96,
    'fact': 'You can purchase almost anything from a vending machine in Tokyo.',
    }

new_york = {
    'country': 'usa', 
    'population': 8.468,
    'fact': 'More than 800 languages are spoken throughout the city.',
    }

cities = {'paris': paris, 'tokyo': tokyo, 'new york': new_york}

for city, city_info in cities.items():
    print(city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + str(city_info['population']) + " mil")
    print("\tFact: " + city_info['fact'])