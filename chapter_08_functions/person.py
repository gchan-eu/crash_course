def build_person(first_name, last_name, age=0):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
pornstar = build_person('anna', 'polina')
print(pornstar)
