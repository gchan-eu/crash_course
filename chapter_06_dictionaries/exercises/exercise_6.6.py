favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary 
# and some that are not.

names = ['nick', 'anna', 'sarah', 'leo', 'phil']

# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking 
# them for responding. If they have not yet taken the poll, 
# print a message inviting them to take the poll.

for name in names:
    if name in favorite_languages:
        print(name.title() + ", thank you for responding to our poll.")
    else:
        print(name.title() + ", you are invited to take our poll.")
