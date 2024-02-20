# to add at the end -> list_items.append(list_item)
# to insert at any position -> list_items.insert(position, list_item)
# to delete at any position -> del list_items[position]
# to delete at the end and store to a variable -> var = list_items.pop()
# to delete at any position and store to a variable -> var = list_items.pop(position)
# to delete by value (1st occurence) -> list_items.remove(list_item)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('kawasaki')
print(motorcycles)

motorcycles.insert(2, 'honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# use pop() to remove last item of the list and store its value to a variable
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# use pop(n) to remove item at position n of the list and store its value to a variable
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('honda')
print(motorcycles)
