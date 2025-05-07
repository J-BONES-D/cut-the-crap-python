"""
This is what is called a 'string literal'. Because it is a string that is
unassigned. Unassigned string literals can be used for multiline comments.
String literals are ignored by the Python Interpreter. A string literal is
surrounded by triple, single or triple double, quotes.
"""

# single-line comments, like this one, begin with the pound symbol, or hashtag... whatever it is called

#############################################################
#                                                           #
#                   Create Variables                        #
#                                                           #
#############################################################

x = 13                          # x is assigned the integer 13
y = "Carbone Hammerschlager"    # y is assigned a string

# use the variables:
print(y, "was once", x, "years old.")

# assign values to multiple variables on one line:
x, y, z = "Red", "Blue", "Green"           # on this line we reassign x and y and create, and assign, z
print(x, y, z)

# assign one value to multiple variables:
x = y = z = "Grey"
print(x, y, z)

# create a collection and unpack its values into variables:
guitars = ["gibson", "ibanez","jackson"]

x, y, z = guitars

print(guitars)
print(x)
print(y)
print(z)



