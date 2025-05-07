"""
Booleans represent truth values in Python and can be either 'True' or 'False'. 
They are used extensively in programming for controlling program flow and
for making decisions.
"""

# operators that result in boolean values:

''' Comparison Operators'''
#       ==      (equal to)

#       !=      (not equal to)

#       >       (greater than)

#       <       (less than)

#       >=      (greater than or equal to)

#       <=      (less than or equal to)

''' Logical Operators'''
#       'and'     Returns True if both operands are True.

#       'or'      Returns True if at least one operand is True.

#       'not'     Returns the opposite boolean value of the operand.


""" conditionally, various data types can be evaluated as boolean values:"""
#   True values:    Non-empty strings, non-zero numbers, non-empty lists, tuples, sets, and dictionaries.

#   False values:   Empty strings, zero, empty lists, tuples, sets, dictionaries and None.

""""""

# evaluate any value with the bool() function:
print(bool("howdy"))    # Output: True
print(bool(""))         # Output: False
print(bool(10))         # Output: True
print(bool(0))          # Output: False

# use boolean statements to control program flow:
x = 13
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

