# start with a dictionary containing at least 1 key-value pair

alien_0 = {'color': 'green', 'points': 5}

# access dictionary's values by keys

print(alien_0['color'])
print(alien_0['points'])

# add new key-value pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25

# print a dictionary

print(alien_0)

# Start with an empty dictionary and add key-value pairs

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

# Modify values

alien_1['color'] = 'purple'

# Remove key-value pairs

del alien_1['points']
print(alien_1)


