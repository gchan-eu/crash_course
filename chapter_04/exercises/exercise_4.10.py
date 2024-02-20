# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

magicians = ['alice', 'david', 'carolina', 'harry', 'beth']
print("The first three items in the list are:")
for magician in magicians[:3]:
    print(magician.title())

# Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.

print("Three items from the middle of the list are:")
for magician in magicians[1:4]:
    print(magician.title())

# Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
    
print("The last three items in the list are:")
for magician in magicians[-3:]:
    print(magician.title())
