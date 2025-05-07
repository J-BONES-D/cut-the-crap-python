"""

String formatting allows you to insert values into strings.

"""

print()

# f-strings (Formatted String Literals):
''' f-strings are the most concise and readable way to format strings. They 
allow embedding expressions inside string literals, prefixed with f or F.
'''

name = "Shawnda"
age = 46
################ f-strings example: ####################
print(f"Her name is {name} and she is {age} years old.")
print()

########################## The str.format() method: ############################## 
''' uses curly braces {} as placeholders. The placeholders can be named or indexed...
'''
employee_name = "Carbone Hammerschlager"
job_title = "Beer Taster"

# unnamed placeholders example:
print("Employee name: {} \tJob Role: {}".format(employee_name, job_title)) # more on the '\t' later. we escaped the character 't' with the backslash 
print()

# using placeholder index example:
print("Employee name: {0} \tJob Role: {1}".format(employee_name, job_title))    # indices begin at zero... employee_name is passed to index[0]
print()

# named placeholders example:
print("Employee name: {name} \tJob Role: {job}".format(name=employee_name, job=job_title))
print()

########################## the % operator (old-style formatting): ###############################
''' this method is considered less readable and more error-prone than f-strings and str.format().
'''
brand = "Kramer"
model = "Nightswan"

print("Brand: %s, Model: %s" % (brand, model))
print()

#########################################
#                                       #
#           Format Specifiers           #
#                                       #
#########################################
"""
Format specifiers can be used inside the curly braces to control the way strings a presented.
You can specify things like alignment, width, precision, and type. 
"""

dogecoin_price = 0.166463

print(f"Dogecoin value to two decimal places: {dogecoin_price:.2f}")    # rounds up or down
print(f"Aligned to 20 spaces: {dogecoin_price:20}")
print()

# format base-10 numbers to base-2:
print(f"Binary representation: {128:b}")
print(f"Binary representation: {64:b}")
print(f"Binary representation: {32:b}")
print(f"Binary representation: {16:b}")
print(f"Binary representation: {8:b}")
print(f"Binary representation: {4:b}")
print(f"Binary representation: {2:b}")
print(f"Binary representation: {1:b}")

print()