favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + 
      favorite_languages['sarah'].title() +
        ".")

# Looping through all key-value pairs

for name, language in sorted(favorite_languages.items()):
    print(name.title() + "'s favorite language is " + 
          language.title() + ".")

# Looping through the keys is the default behavior 
# when looping through a dictionary
    
for name in sorted(favorite_languages):
    print(name.title())

# print a message to some friends
    
print("\nPrint a message to some friends")

friends = ['phil', 'sarah']

for name in sorted(favorite_languages.keys()):
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
        
# find if a person took the poll

print("\nFind if a person took the poll")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through values
    
print("\nThe following languages have been mentioned:")
for language in sorted(set(favorite_languages.values()), reverse=True):
    print(language.title())