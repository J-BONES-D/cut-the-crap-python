######################################################################

'''

There are several built-in data types in Python...

    Text type:          'str'
    Numeric types:      'int', 'float', 'complex'
    Sequence types:     'list', 'tuple', 'range'
    Mapping type:       'dict'
    Set types:          'set', 'frozenset'
    Boolean type:       'bool'
    Binary types:       'bytes', 'bytearray', 'memoryview'
    None type:          'none'

'''

######################################################################

""" Setting Data Types """

# Text Type:            # str data types are created with double or single quotes...
firstName = "Carbone"
lastName = 'Hammerschlager'

# Numeric Types:
x = 13              # type 'int'
y = 34.8            # type 'float'
z = 1j              # type 'complex'

print(x)
print(y)
print(z)

# Sequence Types:
my_list = ["Gibson", "Ibanez", "Kramer"]        # lists are created with square brackets
my_tuple = ('cat', 'dog', 'bird')               # a tuple is created with parenthesis
r = range(14)                                   # creates a range of numbers between 0 and 13

print(my_list[0])
print(my_tuple[2])
for x in r:
    print(x)

# Mapping Type:
my_dict = {"name" : "Carbone", "age" : 54}

print("So, you say that your name is " + my_dict['name'] + "?") # a dictionary item is referenced by its key
print()

# Set Types:    # sets are mutable
my_set = {"red", "blue", "green"}
print("The set 'my_set' is of type: " + str(type(my_set)))
print()

''' Example of a frozenset:'''
# A 'frozenset' is immutable... its items remain constant and can't be changed.
my_frozenset = ({"Indiana", "Michigan", "Ohio"})
print("The frozenset 'my_frozenset' is also of the: " + str(type(my_frozenset)))
print()

# Boolean Types... bool:
''' A boolean value is either, only, "True" or "False"'''
one_boolean = True
two_boolean = False

print("one_boolean is 'True':")
print(one_boolean == True)
print()
print("two_boolean is 'False':")
if two_boolean == False:
    print("Yes 'two_boolean' is False")
else:
    print("two_boolean is not False")

print()
print("one_boolean equals two_boolean is:")
print(one_boolean == two_boolean)
print()

# Binary type examples:
''' working with bytes '''

b1 = b"Hello"
b2 = bytes(4)
b3 = bytes([67, 97, 114, 98, 111, 110, 101])    #ASCII values
b4 = "Hammerschlager".encode()
b5 = bytes.fromhex("47 6F 6F 64 62 79 65")

print(b1, b2, b3, b4, b5, sep=", ")
print()

"""

'bytearray' objects are useful in situations where binary data
needs to be manipulated directly, such as in file I/O operations, 
network programming, or when working with low-level data formats.
They provide a mutable alternative to the immutable 'bytes' type.

"""
# creating a bytearray
my_bytearray_1 = bytearray([67, 97, 114, 98, 111, 110, 101])
my_bytearray_2 = bytearray(b"Hammerschlager")
my_bytearray_3 = bytearray(3)
print(my_bytearray_1, my_bytearray_2, my_bytearray_3, sep=", ")
print()

''' modify a bytearray '''
my_bytearray_2[0] = 68  # 'Hammerschlager' is now 'Dammerschlager'
print(my_bytearray_2)
print()

''' append to a bytearray ''' # add a bang to the end of the bytearray:
my_bytearray_1.append(33)
print(my_bytearray_1)
print()

''' delete from a bytearray ''' # delete the bang
del my_bytearray_1[7]   # deletes the item at index 7 of the bytearray
print(my_bytearray_1)
print()

"""

A 'memoryview' object provides a way to access the internal data of an
object that supports the buffer protocol without copying. This is
particularly useful when working with large objects, as it allows for
efficient manipulation of data without the overhead of creating copies.
Objects that support the buffer protocol include bytes and bytearray

'memoryview' objects are especially beneficial in scenarios requiring 
direct manipulation of binary data, such as image processing or network 
programming, where minimizing memory usage and maximizing performance 
are critical.

"""

# create a bytes object:
my_data = b'abcdefg'

# create a 'memoryview' object from the bytes object:
my_memory_view = memoryview(my_data)

''' access elements of the memoryview object using indexing '''
print(my_memory_view[0])    # outputs the ASCII value of 'a'
print(my_memory_view[2:5])
print()

# Modify elements (if the underlying object is mutable)
my_data_array = bytearray(b'abcdefgh')
my_view_array = memoryview(my_data_array)
my_view_array[0] = 65  # Modify the first element to 'A'
print(my_data_array)

# Release the memoryview
del my_memory_view
del my_view_array

# None Type:
''' Common Uses of None '''
"""

    Function return values: 
        If a function doesn't have a return statement, it implicitly returns None.

    Default argument values: 
        None can be used as a default value for function arguments, allowing the 
        function to handle cases where an argument is not provided.

    Initialization: 
        Variables can be initialized to None when their actual value is not yet known.

    Signaling missing values: 
        None can represent missing or undefined data in data structures.

    ######################################################################################

        It's important to check for None using the 'is' or 'is not' operators, rather 
        than ==, because 'is' checks for object identity, while == checks for equality.

    ######################################################################################


"""

print()
t = None
print(t)
print()
print(type(t))
print()

if t is None:
    print("The variable t is None")