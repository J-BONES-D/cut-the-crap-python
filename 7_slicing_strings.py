"""
String slicing in Python extracts a portion of a string using the syntax string[start:stop:step]. 
The start index is inclusive, the stop index is exclusive, and step determines the increment between indices. 
If omitted, start defaults to 0, stop to the string's length, and step to 1. 
"""

my_string = "Carbone Hammerschlager"

print()

# start from the beginning of the string:
''' the start index is inclusive... the stop index is exclusive '''
print(my_string[0:7])   # output: 'Carbone'... indexing begins at 0
print(my_string[:7])    # start defaults to 0... this line outputs the same as above line of code
print()

# provide a start but, no stop:
''' slices to the end of the string by default '''
print(my_string[8:])
print()

# output every other character:
print(my_string[::2])
print()

""" Negative indices can be used to slice from the end of the string. """

print(my_string[-14:])      # starting from the right of the string, -1 is the first index... index[-14] is 'H'
print(my_string[-14:-8])    # anything beyond index[-8] is ommited
print()

# reverse the string:
print(my_string[::-1])
print()
