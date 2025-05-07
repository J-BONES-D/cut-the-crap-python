"""
List are used to store multiple items in single variable. List are created using
square brackets []. Items in alist are ordered, changeable, and allow duplicates.
Items in a list are indexed with the first item in a list being [0]. The second 
item in the list would be index [1]. A list can contain items of different data
types.
"""

print()

# example list:
my_list = ['carbone', 13.0, False, 54, 'male']

# get the length of a list:
print("There are", len(my_list), "items in the list my_list.")
print()

# lists are of data type list:
print("The data type of my_list is of", type(my_list))
print()

''' You can create a list with the list() constructor. '''
my_list_2 = list(('shawnda', 11.0, True, 46, 'female')) # square brackets were not used here?
print(my_list_2)
print()


#############################################################
#                                                           #
#                   Accessing List Items                    #
#                                                           #
#############################################################

# create a new list:
guitar_brands = ["gibson", "esp", "prs", "ibanez", "kramer", "washburn", "jackson", "ltd"]

# print the fifth item in the list:
print(guitar_brands[4])
print()

# use negative indexing:
print(guitar_brands[-2])
print()

# return a range of indices:
print(guitar_brands[2:5])
print()

# return items from the beginning up to, but not including, 'washburn' and beyond:
print(guitar_brands[:5])
print()

# return items from 'kramer' to the end:
print(guitar_brands[4:])
print()

# a range of negative indices:
print(guitar_brands[-4:-2])     # -2 and beyond is exclusive
print()

# check if an item is in a list:
if "kramer" in guitar_brands:
    print("Yes 'kramer' is in the list guitar_brands.")

print()

#############################################################
#                                                           #
#                   Changing List Items                     #
#                                                           #
#############################################################

print("Our list before changes:")
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

# change the value of index 1:
guitar_brands[1] = "epiphone"
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

# change a range of indices:
guitar_brands[1:4] = ["taylor", "fender", "dean"]
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

''' in the next two examples, items left over to the right of the insert will shift to their new indexes accordingly... '''
# replace the sixth item in the list with two new values:
guitar_brands[5:6] = ["ovation", "indiana"]
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

# insert less items than are replaced:
guitar_brands[1:4] = ["rock jam"]
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

# insert items to a list with a specified index and value with the insert() method:
guitar_brands.insert(1, "taylor")
print(guitar_brands)
print("The length of the list is", len(guitar_brands))
print()

