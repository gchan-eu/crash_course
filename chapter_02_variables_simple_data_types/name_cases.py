name = "Dan"
message = "Hello " + name + ", how are you today?"
print(message)

name = "Linda Fuckface"
message = name.title() + "\n" + name.lower() + "\n" + name.upper()
print(message)

quote = 'Walt Disney once said, "The way to get started is to quit talking and begin doing."'
print(quote)

famous_person = "John Lennon"
message = "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one."
print(famous_person + ' once said, "' + message + '"')

# Demonstrate stripping spaces from a string variable
name = "  Kostas  "
print("\t[" + name + "]\n" + "\t[" + name.lstrip() + "]\n" + "\t[" + name.rstrip() + "]\n" + "\t[" + name.strip() + "]")
