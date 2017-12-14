
# coding: utf-8

# ### Visualize a discrete probability distribution
#
# Fill in the TODOs to get the function working

# In[ ]:
"""
Visualizing a Discrete Probability Distribution
Skills Learned in this Exercise
calculating discrete probability distributions
normalizing a list of values
for loops
Introduction
Now it's time for a challenge. Write a function that, given a list of intervals and total probability, 
calculates the height of each bar. Remember that the sum of the area for all bars should be the total probability.

Here is an example input and output:

a vehicle accident is 5 times more likely from 5am to 10am versus midnight to 5am.
a vehicle accident is 3 times more likely from 10am to 4pm versus midnight to 5am.
a vehicle accident is 6 times more likely from 4pm to 9pm versus midnight to 5am.
a vehicle accident is 1/2 as likely from 9pm to midnight versus midnight to 5am.
The probability of getting in an accident on any given day is .05
The inputs would look like this.

For the hours, you can use 24 hour time hour_intervals = [0, 5, 10, 16, 21, 24]

relative_probabilities = [1, 5, 3, 6, 0.5]

total_probability = 0.05

The output would be the height of each bar:

[0.0006451612903225806,
 0.0032258064516129032,
 0.0016129032258064516,
 0.003870967741935484,
 0.0005376344086021505]
Remember that the values in the probability_intervals variable represent relative probabilities. 
The area of the bar represents the actual probability. And the total probability of getting in an accident is 0.05.
That means the area of all of the bars should add up to 0.05 to represent the probability of getting in an accident. 
You can use this information to figure out the area of each bar, and then you only need to divide each bar area by its 
hourly interval. That will give you the height of the bar.
If you were to visualize the results, it would look something like this:

"""


import matplotlib.pyplot as plt
import numpy as np
import math

def bar_heights(intervals, probabilities, total_probability):

    heights = []
    
    #TODO: sum the relative probabilities
    total_relative_prob = math.fsum(probabilities)
    len_probabilities = len(probabilities)
    for i in range(0, len_probabilities):
        
        #TODO: Looping through the probabilities list,
        #      take one probability at a time and
        #      calculate the area of each bar.  Think about how you can
        #      calculate the area of a bar knowing the total_probability,
        #      relative probability, and the sum of the relative probabilities
        bar_area = (probabilities[i]  / total_relative_prob) * total_probability
        heights.append(bar_area / (intervals[i + 1] - intervals[i]))

        
        # TODO: Calculate the height of the bar and append the value to the
        # heights list.Remember that the area of each bar
        # is the width of the bar times the height of the bar
        #heights.append(0)
        
    return heights


# Run the next cell to test out your function

# In[ ]:

print(bar_heights([0, 5, 10, 16, 21, 24], [1, 5, 3, 6, 0.5], 0.05))


# ### Visualize Results
#
# Once the bar_heights function is working, here is some code to visualize your
# results.

# In[ ]:

hour_intervals = [0, 5, 10, 16, 21, 24]
probability_intervals = [1, 5, 3, 6, 1 / 2]
accident_probability = 0.05

heights = bar_heights(hour_intervals, probability_intervals, accident_probability)
freqs = np.array(heights)
bins = np.array(hour_intervals)
widths = bins[1:] - bins[:-1]
freqs = freqs.astype(np.float)

widths = bins[1:] - bins[:-1]

tick_interval = 1
plt.bar(bins[:-1], freqs, width=widths, align='edge', edgecolor='black', alpha=0.5)
plt.xlabel('Interval')
plt.ylabel('Probability Distribution')
plt.title('Probability Distribution')
plt.xticks(np.arange(min(bins), max(bins) + 1, tick_interval))

plt.show()

