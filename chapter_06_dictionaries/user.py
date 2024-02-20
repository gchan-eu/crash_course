# Dictionary storing information about a user on a web site.

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# Looping through the keys

for key in user_0.keys():
    print('\nKey: ' + key)
    print('Value: ' + user_0[key])

# Looping through the keys is the default behavior 
# when looping through a dictionary

for key in user_0:
    print('\nKey: ' + key)
    print('Value: ' + user_0[key])

# Looping through all key-value pairs

for k, v in user_0.items():
    print('\nKey: ' + k)
    print('Value: ' + v)

