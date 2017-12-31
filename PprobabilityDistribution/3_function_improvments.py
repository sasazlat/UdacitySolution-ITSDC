
# coding: utf-8

# # Improving Your Code
#
# ### Skills in this Excercise
# * Checking for incorrect inputs
# * Improving functions for edge cases
# * Debugging
#
# ### Improving Your Function
#
# Your `probability_uniform` function should work at this point.  But, you
# might run into a couple of problems.
#
# 1.  What happens if you call your function like this: `probability_range(35,
# 20, 0, 360)` ?
# 2.  What happens if you input an angle that is outside the possibilities of
# the bottle's possible outcomes like probability_range(-25, 390, 0, 360)?
# 3.  What if you call your function like this: probability_range('a', 'b', 0,
# 360)?
#
# When writing functions, it's important to think of edge cases or incorrect
# user input.
#
# Here are three more task to help deal with these situations:
# * Make sure the function outputs a valid probability when low_range is
# greater than high_range.  Hint: there is more than one way to do this:
#   * For example, using absolute value
#  * comparing low_range and high_range to see which one is greater
# * Check the inputs to the function to make sure they are not strings.  If the
# user inputted a string, the function should return None.  Optionally, print
# out a message to the user as well explaining why the function put out None.
# This exercise might seem trivial, but if you try to do something like
# `'my_string'/2` in python, you will get an error.  Debugging the errors and
# avoiding them is a key programming skill.
# * Check that the user has only inputted low_range and high_range values that
# are in between minimum and maximum.  If an input is out of the allowed range,
# return None.  Optionally, print out a message to the user as well explaining
# why the function put out None.
#
# Write a function called `probability_range_improved` that takes into account
# these three tasks.

# Fill out the TODOs.  Then run the cells to see if your output is as expected

# In[ ]:
import math

def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    if not all(isinstance(i, (int, float)) for i in [low_range, high_range, minimum, maximum]):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None
    
    # TODO check that low_range is between minimum and maximum
    if not(minimum <= low_range <= maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None
        
    # TODO check that high_range is between min and max
    if not(minimum <= high_range <= maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    # TODO: calulate and return the probability
    # even if low range is greater than high range
    probability = math.fabs(low_range - high_range) / (math.fabs(minimum - maximum))
    return probability


# Run the cell below.  If there are no AssertionErrors, then your code runs as
# expected.  In Python, assert checks whether a statement
# resolves to True or False

# In[ ]:

assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(-100, 300, 100, 500) == None
assert probability_range_improved(105, 700, 100, 500) == None
assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'


