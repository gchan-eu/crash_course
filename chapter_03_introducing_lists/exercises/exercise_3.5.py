invites = ["Martha Stewart", "John Lennon", "Sharon Stone", "Anna Polina"]
message = "I am pleased to invite you to the Christmas Dinner at Hilton Hotel."

# Add a print statement at the
# end of your program stating the name of the guest who can’t make it.

name_out = invites[1]
print(name_out + " can't make it at the dinner.")

# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.

invites[1] = "Nick the Greek"

# Print a second set of invitation messages, one for each person who is still
# in your list.

print("Dear " + invites[0] + ",\n" + message)
print("Dear " + invites[1] + ",\n" + message)
print("Dear " + invites[2] + ",\n" + message)
print("Dear " + invites[3] + ",\n" + message)
