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