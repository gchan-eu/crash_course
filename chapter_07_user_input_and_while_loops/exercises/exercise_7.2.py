seats = input("Hello Sir, how many people are in your dinning group? ")
seats = int(seats)

if seats > 8:
    message = "Sir, you will have to wait for a table."
else:
    message = "Sir, follow me to your table please."

print(message)

