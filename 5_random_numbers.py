"""

Python's random module provides functions for generating pseudo-random numbers. 
These functions can be used to simulate random events, select random elements 
from a sequence, or introduce variability into algorithms.

    Random module functions:

        random.random(): 
            Returns a random float between 0.0 (inclusive) and 1.0 (exclusive).

        random.uniform(a, b): 
            Returns a random float between a (inclusive) and b (inclusive).

        random.randint(a, b): 
            Returns a random integer between a (inclusive) and b (inclusive).

        random.randrange(start, stop[, step]): 
            Returns a randomly selected element from the range created by range(start, stop, step).

        random.choice(seq): 
            Returns a randomly selected element from a non-empty sequence seq.

        random.choices(population, weights=None, k=1): 
            Returns a list of k elements randomly chosen from population, with optional weights for each element.

        random.shuffle(x): 
            Shuffles the elements of the sequence x in place.

        random.sample(population, k): 
            Returns a list of k unique random elements chosen from population.

    ### In order to use 'random' functions, one must import the module. ###

"""

import random

print()

# random.random():
print(random.random()) # generates a random float numeric between 0.0 and 1.0
print()

# random.uniform(a, b):
print(random.uniform(1, 13)) # generates a random float numeric between 1.0 and 13.0
print()

# random.randint(a, b):
print(random.randint(1, 13)) # generates a random integer numeric between 1 and 13
print()

# random.randrange(start, stop[, step]):
print(random.randrange(0, 71, 2)) # generate a random even number between 0 and 70
print()

# random.choice(seq):
''' In this example we choose a random element from a list '''
my_list = ['Jackson', 'Ovation', 'Kramer', 'Ibanez']
print(random.choice(my_list))
print()

# random.choices(population, weights=None, k=1):
''' 
The random.choices() function in Python's random module is used to select 
multiple random elements from a sequence (like a list, tuple, or string) 
with replacement, meaning the same element can be chosen multiple times. 
It offers flexibility by allowing specification of weights for each element, 
influencing their probability of selection.
'''

## Basic usage: select 3 random elements with replacement:
result_1 = random.choices(my_list, k=3)
print(result_1)
print()

## Weighted selection: 'Kramer' is twice as likely as others to be selected:
weights = [1, 1, 2, 1]
result_2 = random.choices(my_list, weights=weights, k=3)
print(result_2)
print()

## Cumulative weights:
cum_weights = [2, 3, 4, 5]
result_3 = random.choices(my_list, cum_weights=cum_weights, k=3)
print(result_3)
print()

"""
    If no weights are specified, each element has an equal chance of being selected. 
    The k parameter determines the number of elements to choose. Using random.choices() 
    is particularly useful in simulations, data sampling, and scenarios where weighted 
    random selection is needed.
"""

# random.shuffle(x):
random.shuffle(my_list)
print(my_list)
print()

# random.sample(population, k):
print(random.sample(my_list, 2)) # gets two, unique, random elements from a list
print()

##########################################################################################
'''
It is important to note that the random module generates pseudo-random numbers, which are 
not truly random but are sufficient for many applications. For applications requiring 
high-security randomness, consider using the secrets module.
'''
##########################################################################################