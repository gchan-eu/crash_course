# Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

pornstars = ['Clara Mia', 'Anna Polina', 'Alexis Tae', 'Maya Woulfe']

# Add at the end

pornstars.append('Sara Diamante')

# insert at 3rd position

pornstars.insert(2, 'Alice Martin')
print(pornstars)

# delete 4th pornstar

del pornstars[3]
print(pornstars)

# delete 1st one and print the name

name = pornstars.pop(0)
print(name + " is deleted.")
print(pornstars)

# delete by name Sara Diamante

pornstars.remove('Sara Diamante')
print(pornstars)

# sort alphabetically

pornstars.sort()
print(pornstars)

# sort alphabetically in reverse order temporarily

print(sorted(pornstars, reverse=True))

# count the items

print("There are " + str(len(pornstars)) + " pornstars in the list.")
