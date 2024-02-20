invites = ["Martha Stewart", "John Lennon", "Sharon Stone", "Anna Polina"]

# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# Add a print statement to the end of your program informing people that you found a
# bigger dinner table.

message = "I am pleased to inform you that we have secured a bigger dinner table for our Christmas Dinner."

print("Dear " + invites[0] + ",\n" + message)
print("Dear " + invites[1] + ",\n" + message)
print("Dear " + invites[2] + ",\n" + message)
print("Dear " + invites[3] + ",\n" + message)

# Use insert() to add one new guest to the beginning of your list.

invites.insert(0, "Agatha Vega")

# Use insert() to add one new guest to the middle of your list.

invites.insert(3, "Clemence Audiard")

# Use append() to add one new guest to the end of your list.

invites.append("Clara Mia")

# Print a new set of invitation messages, one for each person in your list.

message = "I am pleased to invite you to the Christmas Dinner at Hilton Hotel."

print("Dear " + invites[0] + ",\n" + message)
print("Dear " + invites[1] + ",\n" + message)
print("Dear " + invites[2] + ",\n" + message)
print("Dear " + invites[3] + ",\n" + message)
print("Dear " + invites[4] + ",\n" + message)
print("Dear " + invites[5] + ",\n" + message)
print("Dear " + invites[6] + ",\n" + message)
