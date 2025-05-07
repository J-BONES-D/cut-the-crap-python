"""
List in Python are mutable( meaning 'changeable) ordered( indexed) sequences of items. 
List are coded by enclosing comma-separated values( items) within square brackets []. 
Lists can contain items that are of different data types or Python objects.
"""

# create a list:
colors = ["red", "orange", "yellow"]

# output the list:
print()
print("The list before modifications:")
print(colors)
print()

# append items to a list: ... add items to the end of the list
colors.append("green")
print("The list after modification:")
print(colors)
print()

# create a second list:
more_colors = ["blue", "indigo", "violet"]

# extend lists: ... append elements from one list to another
colors.extend(more_colors)
print("The colors of a rainbow are:")
print(colors)
print()

# create a tuple:
color_tuple = ("brimstone", "chartreuse")

# add any kind of iterable with the extend() method:
colors.extend(color_tuple)
colors.extend(range(3))

print(colors)
print()

#########################################################
#                                                       #
#               Removing List Items                     #
#                                                       #
#########################################################

# create a new list:
elements = ["earth", "wind", "water", "fire"]
print("Contents of the 'elements' list:")
print(elements)
print()

# remove a specified item with the remove() method:
elements.remove("wind")
print(elements)
print()

# lets put it back:
elements.insert(1, "wind")
print(elements)
print()

# make use of the pop() method:
elements.pop(1)     # if the index was not provided as a parameter, the last item would be popped from the list
print("The wind is gone again...")
print(elements)
print()

# clear a list of its items:
elements.clear()
print("Now there are no elements left:")
print(elements)
print()

print("Here is our colors list from earlier:")
print(colors)
print()

# delete specific items with del():
del colors[-3]
del colors[-2]
del colors[-1]
print("We have removed all the numbers from the colors list:")
print(colors)
print()

print("Back to the rainbow...")
del colors[7]
del colors[7]
print(colors)
print()

