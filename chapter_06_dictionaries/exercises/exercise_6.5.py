rivers = {
    'nile': 'egypt', 
    'danube': 'slovakia', 
    'amazon': 'brazil', 
    'yangtze': 'china',
    'mississippi': 'usa'
    }

for river, country in rivers.items():
    print("The " + river.title() + 
          " river runs through " + country.title() + ".")
    
# Use a loop to print the name of each river 
# included in the dictionary.

print("\nRivers:")  
for river in sorted(rivers):
    print(river.title())

# Use a loop to print the name of each country 
# included in the dictionary.

print("\nCountries:")    
for country in sorted(set(rivers.values())):
    print(country.title())