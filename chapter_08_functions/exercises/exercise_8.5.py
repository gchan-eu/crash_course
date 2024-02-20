def describe_city(name, country='USA'):
    print(name.title() + " is in " + country.title() + ".")

describe_city('Oregon')
describe_city("Cologne", "Germany")
describe_city(name='athens', country='greece')
describe_city(country='italy', name='venice')