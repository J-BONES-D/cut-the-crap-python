"""
List comprehension is a shorter syntax for creating a list
based on the values of an already-existing list.
"""

# create a list:
guitars = ["kramer", "esp", "ovation", "washburn", "jackson"]

######################################################
# example creating a list without list comprehension:#
######################################################
new_list = []

for x in guitars:
    if "a" in x:
        new_list.append(x)

print()
print(new_list)
print()

#############################################
# create a new list with list comprehension:#
#############################################

# syntax of a list comprehension:
'''

    new_list = ['expression' for 'item' in 'iterable' if 'condition']

'''
#############################################################################################################################

#   expression:     This is the operation that is performed on each item going into the new list.
#   item:           This is a variable representing each element in the iterable.
#   iterable:       This is the sequence being iterated over (e.g., list, tuple, or range).
#   condition:      A filter that determines whether or not an item is included in the new list (the condition is optional).

#############################################################################################################################

new_list_2 = [x for x in guitars if "a" in x]

print()
print(new_list_2)
print()

# create a new list using 'range' without a 'condition':
cubes = [x**3 for x in range(6)]
print(cubes)
print()

# create a new list using 'range' with a 'condition':
odd_cubes = [x**3 for x in range(6) if x % 2 != 0]
print(odd_cubes)
print()

print("Until next time, developer...")