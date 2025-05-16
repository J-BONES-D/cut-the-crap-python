"""
Using the concatenation operator(+) or making use of the extend() method are the more efficient ways of joining lists in Python. 
Using the append() method within a loop and list comprehension are other means for joining lists.
"""

print()

# create two lists:
list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]

####################
# use concatenation:
####################
''' Concatenates two lists, creating a new list with all elements from each list. '''
list_3 = list_1 + list_2

print("list_1:", list_1)
print()
print("list_2:", list_2)
print()
print("list_3:", list_3)
print()


##########################
# use the extend() method:
##########################
''' Adds all of the elements from one list to the end of another list. This modifies the original list.'''
list_1.extend(list_2)

print("list_1 is now:", list_1)
print()

##########################
# use the append() method:
##########################

# create an empty list:
empty_list = []

for x in list_3:
    empty_list.append(x)

print("empty_list isn't empty?")
print()
print("\t", empty_list)
print()

print("Time for 'tuples' developer!")