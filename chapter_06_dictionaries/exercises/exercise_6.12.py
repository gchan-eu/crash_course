# List inside dictionary

favorite_toys = {
    'sarah': ['vibrator'], 
    'polina': ['dildo', 'vibrator'], 
    'amanda': ['butt plug', 'dildo', 'vibrator', 'anal dildo'], 
    'cherry': ['dildo', 'double dong'], 
    'vanessa': ['strapon', 'butt plug'],
    'suzy': ['butt plug']
    }

for name, toys in favorite_toys.items():
    if len(toys) == 1:
        print(name.title() + "'s favorite toy is:")
    else:
        print(name.title() + "'s favorite toys are:")
    for toy in sorted(toys):
        print("\t" + toy.title())