"""

With Python, a list can be sorted in ascending or descending order with
the sort() method or the sorted() function.

    sort():     This method modifies the list in-place.
    sorted():   This function returns a new sorted list, leaving the original list unchanged.

    /** Comparisons between integers and strings is not supported when sorting! **/

"""

# create some lists:
word_list = ["program", "python", "cool", "people"]
numerics = [13, 5, 4, 11, 78, 71, 0]
mixed_list = ['one', 1, 'two', 2, 'three', 3]
print()

###########################################################
# the sorted() function leaves the original list unchanged:
###########################################################

# list of strings:
print(sorted(word_list))
print()
print(word_list)    # the unchanged list
print()

# list of integers:
print(sorted(numerics))
print()
print(numerics)    # the unchanged list
print()

# mixed list of strings and integers:
''' comparison of integers and strings is not supported... convert list to string type:'''
print(sorted(str(mixed_list)))
print()
print(mixed_list)    # the unchanged list
print()

#####################################
# the sort() method changes the list:
#####################################

# list of strings:
print(word_list)
word_list.sort()
print()
print(word_list)    
print()

# list of integers:
print(numerics)
numerics.sort()
print()
print(numerics)
print()

""" The sort() method can not be used with list containing different data types. """
''' Trying to use the sort() method with the list mixed_list would raise an exception. '''

##########################
# sort list descending...:
##########################

''' using the sorted() function: '''
print(sorted(word_list, reverse=True))
print()
print(sorted(numerics, reverse=True))
print()

''' using the sort() method: '''
word_list.sort(reverse=True)
print(word_list)
print()
numerics.sort(reverse=True)
print(numerics)
print()

# simply reverse the order of the list:
word_list.reverse()
numerics.reverse()

print(word_list)
print(numerics)

print()

""" by default, these sorting methods and functions are case-insensistive. """
''' Capitals are sorted first... '''

# create another list:
grandbabies = ["stetson", "Kendyl", "Scarlette", "hollins", "Truette", "riggins"]

print(sorted(grandbabies))
print()

grandbabies.sort()
print(grandbabies)
print()


"""
The sort() method and the sorted() function can accept a key argument.
The 'key' argument specifies a function to be called on each list element 
before making any comparisons.
"""
# a case-insensitive sort:
grandbabies.sort(key=str.lower)
print(grandbabies)

print()
print("One step closer developer!")