"""
There are few ways of looping through list:

        > Iterate directly over the elements of the list with a 'for' loop.

        > Iterate through the indices of a list with a 'for' loop.

        > Use enumerate() function.
        >>>>> This functions gives the index and value of each item in the list.

        > Use a 'while' loop.
        >>>>> A developer must use index management, or a counter, to terminate the loop.
"""

print()

# create lists to use with the examples:
guitar_brands = ["Kramer", "Gibson", "Ovation", "Prs", "Esp"]
guitar_models = ["Nightswan", "Les Paul", "Celebrity", "Custom", "Ltd"]


#################################################
#                                               #
#               'for' Loops                     #
#                                               #
#################################################

# iterate the list itself:
for axe in guitar_brands:
    print(axe)

print()

# utilize indices with the range() function:
for i in range(len(guitar_brands)):
    print(guitar_brands[i])

print()


#################################################
#                                               #
#          Using 'enumerate' with 'for'         #
#                                               #
#################################################

for index, item in enumerate(guitar_brands):
    print(f"Index: {index}, Value: {item}")

print()

for index, item in enumerate(guitar_brands, start=1):   # you can specify the index start number...
    print(f"Index: {index}, Value: {item}")

print()


# iterate through two lists simultaneously with the zip() function:
for brand, model in zip(guitar_brands, guitar_models):
    print(brand, model)

print()


# an example using 'list comprehension':        # more on this later...
''' list comprehension is basically a short-hand version of the 'for' loop '''
[print(axe) for axe in guitar_brands]


print()


#################################################
#                                               #
#            The 'while' Loop                   #
#                                               #
#################################################

''' When using a "while" loop, some sort of counter must be coded as well... '''

i = 0   # this is the counter

while i < len(guitar_brands):
    print(guitar_brands[i])
    i = i + 1           # here the counter value is incremented by 1 in each loop

print()