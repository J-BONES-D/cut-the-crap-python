"""

Strings are simply characters placed between either 'single' or "double" quotes.

"""

# double quotes example:
print("Carbone")

# single quotes example:
print('Hammerschlager')
print()

# using quotes inside quotes:
print("It's ok to use single quotes inside double quotes or vise versa.")
print('His real name is Jason but, sometimes goes by "Carbone."')
print()

# strings are actually arrays: A strings elements can be referenced by index...
my_string = "Carbone HammerSchlager"
print(my_string[8]) # indices begin at 0
print()

# loop through a string using a 'for' loop:
for letter in my_string:
    print(letter)

print()

# return the length of a string:
print(len(my_string))
print()

# check if a string is within a string:
print("Car" in my_string) # returns 'True'

# check if a string is not in a string:
print("Cat" in my_string) # returns 'False'
print()