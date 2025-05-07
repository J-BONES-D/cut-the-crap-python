"""
Concatenation is the act of combining two or more strings together into a single string.
There is more than one way to acheive this:

        Using the + operator: 
            The + operator joins two strings together.

        Using the += operator:
            The += operator appends one string to the end of another.

        Using the join() method: 
            The join() method takes an iterable as an argument and returns a single string, 
            with the elements of the iterable joined by the string on which the method is called.
            This method is good to use when the amount of strings being used is not known.
        
        Using f-strings (formatted string literals): 
            f-strings provide a way to embed expressions inside string literals.

        Using the % operator (old-style formatting): 
            You may come across this method in older code.

        /** You can concatenate non-string data types by using 'type conversion' */

"""

print()

# create some strings:
a = "Emerson"
b = "Bigguns"
age = 54

# Using the + operator:
full_name = a + b   # this line of code returns 'EmersonBigguns'... notice there is no space between the concatenated strings
print(full_name)
print()
full_name = a + " " + b # change full_name to include a space
print(full_name)
print()

# Using the += operator:
a += b      # this actually changes the value stored in the 'a' variable.
print(a)    # again, no space is included...
print()

# create an iterable:
my_list = ['Carbone', ' ', 'Hammerschlager']

# Using the join() method:
user = "".join(my_list)     # here we join the list to an empty string, creating a new string
print(user)
print()

# Using f-strings (formatted string literals):
username = f"{a} {b}"
print(username)     # recall that the variable 'a' was changed earlier...
print()
username = f"{a[:-7]} {b}"  # fixed the problem with 'slicing'... you could've just changed the value of 'a'
print(username)
print()

# Using the % operator (old-style formatting):
first_name = "PeeWee"
last_name = "Herman"
first_and_last = "%s %s" % (first_name, last_name)
print(first_and_last)
print()

# Concatenate a non-string to a string with type conversion:
print(username + " is " + str(age) + " years old.")
print()