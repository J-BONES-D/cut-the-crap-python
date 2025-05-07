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

