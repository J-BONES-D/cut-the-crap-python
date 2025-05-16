"""
There are several ways to copy lists in Python...
"""

print()

# create a list:
animals = ["dog", "cat", "bird", "fish", "human"]

print("The original list, animals, contains:")
print(animals)
print()

# use the built-in copy() method:
new_list_1 = animals.copy()

print("The contents of new_list_1 are:")
print(new_list_1)
print()

# use the built-in list() function:
new_list_2 = list(new_list_1)           # assigns a copy of new_list_1 to new_list_2

print("The contents of new_list_2 are:")
print(new_list_2)
print()

# use a slice to make a copy of a list:
new_list_3 = animals[:]

print("The contents of new_list_3 are:")
print(new_list_1)
print()

print("Off to 'join' developer!")