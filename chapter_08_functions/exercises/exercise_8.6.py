def city_country(name, country):
    return_value = name.title() + ', ' + country.title()
    return return_value

city = city_country(name='rio', country='brazil')
print(city)
city = city_country(name='milan', country='italy')
print(city)
city = city_country(name='geneva', country='switzerland')
print(city)