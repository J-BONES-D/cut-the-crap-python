"""
Strings in Python are immutable. Immutable means they cannot be changed directly. 
To modify a string, you must create a new string with the desired changes.
There are many built-in methods for modifying strings. Here is some of them:

    upper(): Converts the string to uppercase.
    
    lower(): Converts the string to lowercase.
    
    strip(): Removes leading and trailing whitespace.
    
    replace(old, new): Replaces all occurrences of a substring old with a substring new.
    
    split(separator): Splits the string into a list of substrings based on a specified separator.

"""

# create some strings:
a = "carbone"
b = "hammerschlager"
c = "Hello, Developer!"

print()

# return a string in uppercase:
print(a.upper())
upper_b = b.upper()
print(upper_b)
print(c.upper())
print()

# return a string in lowercase:
print("The value of the variable upper_b is: " + upper_b)
print("After using the lower() method, upper_b is temporarily: " + upper_b.lower())
print("The value of upper_b is", upper_b)
print()

another_string = "          Ten leading whitespaces and ten trailing whitespaces          "

# remove whitespaces with the strip() method:
print(another_string.strip())
print()

# replace part of a string:
print(c.replace("Hello", "Howdy"))
print()

# split a string:
''' returns a list of the items in a string seperated by a specified seperater '''
print(c.split(","))
print(another_string.strip().split(" "))
print()

print(c.replace("Hello", "Goodbye"))
print()