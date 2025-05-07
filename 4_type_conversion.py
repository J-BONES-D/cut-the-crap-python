'''

Type conversion in Python refers to changing a variable's data type. It's essential 
for performing operations that require specific data types or for ensuring data 
compatibility. Python supports two main types of conversion: implicit and explicit.

'''

######  Implicit Type Conversion (Coercion):

"""

    Python automatically converts data types in certain situations to prevent data loss. 
    This usually happens when performing operations between different data types. 
    For example, when adding an integer and a float, Python will implicitly convert the 
    integer to a float.

"""

print()

int_num = 10
float_num = 3.0

added_nums = int_num + float_num

print(added_nums)
print(type(added_nums)) # verify the type of objects with the type() function

print()

######  Explicit Type Conversion (Casting):

"""

    Explicit type conversion occurs when the programmer manually converts a data type using built-in functions.

        int(): Converts to an integer data type.
        
        float(): Converts to a floating-point data type.
        
        str(): Converts to a string data type.
        
        bool(): Converts to a boolean data type.
        
        list(), tuple(), set(), dict(): Convert to list, tuple, set, or dictionary, respectively.

"""

# Convert a string to an integer:
my_string = "413"
str_to_int = int(my_string)
print(str_to_int)
print(type(str_to_int))
print()

# Convert from float to integer:
''' When you convert from a float to an integer, the decimal part is truncated... it drops off. '''
float_num = 4.13
float_to_int = int(float_num)
print(float_to_int)
print()

# Convert from integer to string:
int_num = 13
int_to_str = str(int_num)
print(int_to_str)
print(type(int_to_str))
print()

# Convert a list into a tuple:
my_list = [4, 13, 71]
list_to_tuple = tuple(my_list)
print(list_to_tuple)
print(type(list_to_tuple))
print()

# Convert a string to a list:
new_string = "Carbone"
str_to_list = list(new_string)
print(str_to_list)
print(type(str_to_list))
print()