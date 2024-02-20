# A list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing frogs
    
frogs = []

# Make 30 small frogs

for n in range(30):
    new_frog = {'size': 'small', 'points': 5, 'speed': 'slow'}
    frogs.append(new_frog)

for frog in frogs[0:3]:
    if frog['size'] == 'small':
        frog['size'] = 'medium'
        frog['points'] = 10
        frog['speed'] = 'average'
    elif frog['size'] == 'medium':
        frog['size'] = 'large'
        frog['points'] = 15
        frog['speed'] = 'high'

for frog in frogs[:5]:
    print(frog)
print('...')
print("Total number of frogs is " + str(len(frogs)))

