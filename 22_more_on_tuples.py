"""
Tuples are immutable but, there are ways to modify tuples...
"""

print()

##############################################################################
# convert the tuple into a list, make changes, then convert back to a tuple...
##############################################################################

# create a tuple:
x = ("peach", "pear", "plum")

# create a list out of the tuple above:
y = list(x)

# make edits to the list:
y[0] = "orange"
y[1] = "apple"
y[2] = "banana"

# create a tuple from the modified list:
x = tuple(y)

print(x)
print()


######################################################################
# add items to a tuple:
######################################################################
''' use the append() list method '''

# create another tuple:
this_tuple = ("red", "white", "green")

tuple_to_list = list(this_tuple)    # convert tto a list

tuple_to_list.append("blue")

this_tuple = tuple(tuple_to_list)   # convert back to a tuple

print(this_tuple)
print()


#####################################################################
# remove items from a tuple:
#####################################################################

# again, convert the tuple into a list:
y = list(this_tuple)

# edit the list:
y.remove("green")

this_tuple = tuple(y)

print(this_tuple)
print()

# delete a tuple entirely:
''' after execution of the following statement, trying to print the tuple afterwards would cause an error... '''
del x

#print(x)


#####################################################################
# concatenate two tuples:
#####################################################################

one_tuple = ("legos", "puzzles", "lincoln logs")
two_tuple = ("budweiser", "steel reserve", "modelo")

one_tuple += two_tuple

print(one_tuple)
print()


####################################################################
# unpacking tuples:
####################################################################
''' when you put items into a tuple, you are packing the tuple... '''

# pack a tuple:
grades = ("freshman", "sophmore", "junior", "senior")

# unpack a tuple: ''' extract items in a tuple into variables '''
#################################################################
(ninth, tenth, eleventh, twelveth) = grades

print(ninth)
print(tenth)
print(eleventh)
print(twelveth)

print()

# unpacking a tuple using the asterisk * :
##########################################
''' if the number variables being assigned is less than
number of the items in the tuple, add a preceding '*' to
the variable being assigned and the overloaded items
will be assigned to that vaiable as a list.
'''
# create a tuple:
fruits = ("grape", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green, yellow, red)
print()


# create another tuple:
more_fruits = ("grape", "mango", "papaya", "pineapple", "cherry")

(green, *tropical, red) = fruits

print(green)
print(tropical)
print(red)

print()


######################
# loop through tuples:
######################

# use a for loop:
for x in fruits:
    print(x)

print()

for x in range(len(more_fruits)):
    print(more_fruits[x])

print()


# use a while loop:
counter = 0

while counter < len(more_fruits):
    ele = more_fruits[counter]
    print(ele + " is delicious!")
    counter += 1

print()


##################################
# join tuples:
##################################

# use concatenation:
all_fruits = fruits + more_fruits
print(all_fruits)

print()

# use replication:
two_fruits = fruits * 2
print(two_fruits)

print()


####################################################
# some tuple methods:
####################################################
""" Tuples are immutable, so methods like append(), extend(), insert(), remove(), or pop() won't work. """
''' convert to a list remember... '''

# use the count() method:
''' returns the number of times an item occurs in a tuple '''
print("'grape' occurs in the two_fruits tuple", two_fruits.count("grape"), "times...")
print()


# use the index() method:
''' returns the index location of the first occurrence of an item in a tuple. '''
print(all_fruits.index("grape"))    # returns '0'
print()

""" research tuple methods for more... """

print("Next up on the set is 'Sets'")
print()