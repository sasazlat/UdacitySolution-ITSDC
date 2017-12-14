
# coding: utf-8

# # Uniform Probability Distribution
#
# ### Skills Learned in this Exercise
# * writing functions in python
# * calculating uniform continuous distributions
# * calculating probabilities from continuous uniform distributions.
#
# ### Continuous Uniform Distribution
#
# From the lesson videos, the wheel of fortune and spinning bottle examples
# both had continuous uniform distributions.  You spin, and the arrow or bottle
# had an equal chance of stopping anywhere between 0 and 360 degrees.
#
# For this first programming exercise, write a function that calculates the
# probability that the arrow will stop between two angles.  You'll want this
# function to work with any continuous uniform distribution, so the function
# will have four inputs:
# * `low_range` representing the first angle
# * `high_range` representing the second angle
# * `minimum` representing the minimum value of the distribution (0 for the
# spinning example)
# * `maximum` representing the maximum value of the distribution (360 for the
# spinning example)
#
# The output should be the probability that the arrow stops between low_range
# and high_range.

# # Uniform Probability Distribution Function
#
# The probability_uniform function calculates the probability of an event
# given a range of values from a uniform continuous probability distribution.
#
# - low_range is the low end of the region of interest
#
# - high_range is the high end of the region of interest
#
# - minimum is the minimum value of the uniform probability
#   distribution (0 for a spinning wheel)
#
# - maximum is the maximum value of the uniform probability
#   distribution (360 for a spinning wheel).
#

# In[ ]:

import math

def probability_uniform(low_range, high_range, minimum, maximum):
    
    ## TODO: Calculate the probability of an event occurring
    ## between low_range and high_range.
    ## Assume the user has given valid inputs such that low_range < high_range.
    ##   minimum < maximum
    ##

    probability = 0
    
    probability = math.fabs(low_range-high_range)/(math.fabs(minimum-maximum))
    
    return probability


print(probability_uniform(35, 20, 0, 360))
    



# In[ ]:


## TODO: Test your results by running this cell.
## If the cell produces no output, your answer was as expected
assert "{0:.2f}".format(probability_uniform(15, 305, 0, 360)) == '0.81'
assert "{0:.2f}".format(probability_uniform(1, 5, 0, 10)) == '0.40'


