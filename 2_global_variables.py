'''
This section is about "Global Variables." A global variable's scope
is the entire program. This means that it can be accessed or modified
anywhere within the code, including inside functions.
'''

# create global variables named 'x' and 'y'
x = "Carbone"
y = "IN LOVE!"

def myfunc():
    print("Hey, you are not " + x)   # the value of 'x' is concatenated to the string

print()

myfunc()

print()

""" Define another function """
def myfunc_2():
    y = "twitterpated..."      # overrides 'y' inside the function... does not change the global variable
    print("You are " + y)

myfunc_2()
print("Just kidding... YOU ARE " + y)

print()