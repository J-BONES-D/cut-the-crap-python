"""
A tuple is a collection of ordered, immutable sequences of elements. 
You define a tuple by enclosing comma-separated elements within parentheses (). 
Tuples cannot be modified after creation.
Tuples allow duplicate elements.
Tuples are indexed the same as lists.
Their elements cannot be changed, added, or removed.
"""

print()

#################
# create a tuple:
#################
this_tuple = ("peach", "pear", "plum")

''' when creating a tuple with a single item... add a comma after that item. '''
one_item_tuple = ("starfruit",)

###############################################
# create a tuple using the tuple() constructor:
###############################################
new_tuple = tuple(("muskmellon", "cantalope", "watermelon"))

print("this_tuple:\t", this_tuple)
print("one_item_tuple:\t", one_item_tuple)
print("new_tuple:\t", new_tuple)

print()

##############################
# check the length of a tuple:
##############################
print("The number of items in the tuple new_tuple is:", len(new_tuple))
print()

#################################
# check the data type of a tuple:
#################################
print("The data type of new_tuple is of:", type(new_tuple))
print()


######################################################################
# accessing tuple items:
######################################################################
''' Accessing items in a tuple works the same as it does for list. '''

print("One of my favorite fruits is", new_tuple[2])
print()
if "muskmellon" in new_tuple:
    print("I thought you liked muskmellon?")

print()
print(new_tuple[-3:])
print(new_tuple[0:])
print(new_tuple[:])
for x in new_tuple:
    print(x)

print()

print("Check out 'more_on_tuples'")