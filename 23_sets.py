"""
A set is a collection, or sequence, that is...

    # unordered

    # unchangeable but, you can add and remove items

    # unindexed

    /* sets are coded using curly braces */

    /* duplicates are NOT allowed */

        # 'True' and '1' are considered duplicates
        # 'False' and '0' are also considered duplicates

"""

# create  a simple 'set':
my_set = {"kramer", "esp", "ovation"}   # more guitars

# create a set using the set() constructor:
this_set = set(("red", "blue", "green"))    # notice the use of parenthesis instead of curly braces when using a constructor...

print()

#############################################################################
# Accessing Set Items:
#############################################################################
""" /* You cannot access set items by referring to an index or key... */ """

# loop through a set with a for loop:
for x in this_set:
    print(x)

print()

# check if an item is 'in' a set:
print("orange" in this_set)
print("blue" in this_set)

print()

if "orange" in this_set:
    print("Orange is in the set this_set.")
else:
    print("There is no orange in the set this_set.")

print()


################################
# add items to a set:
################################
this_set.add("purple")
this_set.add("purple")  # duplicates are not allowed...

print(this_set)

print()


# create two new sets:
letters_set = {"A", "B", "C"}
numbers_set = {1, 2, 3}

# add items from one set to another with the update() method:
letters_set.update(numbers_set)     # recall that sets are unordered
print(letters_set)
print()

# add any iterable to a set with the update() method:
# create a set:
fruit_set = {"papaya", "noni", "coconut"}

# create a list:
fruit_list = ["kiwi", "soursop"]

# use the update() method:
fruit_set.update(fruit_list)

print(fruit_set)
print()


######################################################
# Removing set items:
######################################################

# the remove() method:
''' if the item being removed does not exist in the set, an exception will be raised. '''
fruit_set.remove("noni")
print(fruit_set)
print()

# the discard() method will not raise an exception if the item is not found:
fruit_set.discard("jackfruit")
print(fruit_set)
print()

# the pop() method removes a random item and returns that item:
x = fruit_set.pop()
print(x)
print(fruit_set)
print()

# the clear() method empties the set:
fruit_set.clear()
print("After clearing the set fruit_set, fruit_set returns:")
print(fruit_set)
print()

# using the del() method removes the set entirely:
''' if you try to access the set after deletion, an exception will be raised. '''
del fruit_set

''' uncomment the following and see for yourself '''
#print(fruit_set)


###############################
# Loop through sets with 'for':
###############################

# create a new set:
new_set = {"beer", "wine", "vodka", "tequila", "bourbon", "whiskey"}

# loop with 'for':
for x in new_set:
    print(x)

print()

# use the enumerate() function with 'for':
for index, item in enumerate(new_set):
    print(f"Index: {index}\tItem: {item}")

print()

print("Lets join sets developer in 24_joining_sets.py!")