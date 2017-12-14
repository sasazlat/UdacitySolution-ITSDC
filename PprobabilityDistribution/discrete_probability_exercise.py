
# coding: utf-8

# # Discrete Probability Exercise
#
# You have two dice.  These are fair, six-sided dice with the values one
# through six.
#
# You take the dice, and you roll them.  Then you take the sum of the two
# numbers.  For example, if you roll the dice and get 5 and 4, then the sum
# would be 9.
#
#
# ![alt text](dice.png)
#
#
# Now, you're curious to know what sum or sums are most likely to occur.  So
# you decide to repeat your experiment two-thousand times and then analyze the
# results.
#
# You roll the dice over and over again.  Each time you write down what sum you
# got.

# # Results of your experiment
#
# Here are the results of your experiment.  The left hand column shows the sum
# and the right hand column shows how many times that sum appeared over your
# two-thousand trials:
#
# | Dice Sum | Count |
# |----------|-------|
# | 2 | 54 |
# | 3 | 111 |
# | 4 | 163 |
# | 5 | 222 |
# | 6 | 277 |
# | 7 | 336 |
# | 8 | 276 |
# | 9 | 220 |
# | 10 | 171 |
# | 11 | 111 |
# | 12 | 59 |
#
# Your task is to analyze these results and turn them into a discrete
# probability distribution.
#
# Follow along the Ipython notebook completing each exercise and demo.  We've
# provided answers to the exercises in the next part of the lesson.

# # Exercise: Create a List
#
# In order to analyze these results, you'll need to put them into some sort of
# data structure.  For this case, use a Python list.
#
# A Python list is just what it sounds like: a list of values.
# If you had the values `1 5 19 25 and 30`, here is how you could put them in a
# Python list:
#
# ```python
# listexample = [1, 5, 19, 25, 30]
# ```

# In[ ]:


####
# TODO: Create a Python list of the values in the 'Count' column.
# Your list should start with 54 and follow the same order
# as the data in the column: 54, 111, 163, etc.
###
count_data = [54,111,163,222,277,336,276,220,171,111,59]


# # Demo: Print Your List
#
# Run the code cell below to print out your list.  This cell uses a for loop to
# iterate through every value in your list.  Pay attention to the syntax
# because you'll be writing your own for loop soon.

# In[ ]:


# Run this code cell.  You do not need to change anything

# A for loop to print out every value in the count_data list
# The len() function determines the size of the list
# The range() function creates an integer
#           list from 0 to len(count_data).
for i in range(len(count_data)):
    print(count_data[i])


# # Exercise: Sum the Counts
#
# Let's double check how many trials you actually did.  In this exercise,
# you'll calculate the sum of your count_data list.  This sum represents the
# total number of times you rolled the dice.
#
# Finding the sum of a Python list is relatively straightforward.  The syntax
# is:
# ```
# sum(list_variable)
# ```

# In[ ]:


###
# TODO: calculate the sum of the count_data list
#     and put the sum in the total_count variable
###
total_count = sum(count_data)

# This will print out the result
print(total_count)


# # Demo: Visualization of the Data
#
# If you look at the data, you can already tell which case has the highest
# probability of occurring: 7.
#
# And it also looks like the probability distribution is symmetrical with 6 and
# 8 having the same probability, 5 and 9, etc.  Here is a visualization of the
# data:
#
# ![Visualization](visualization.png)
#

# But is this visualization a discrete probability distribution?  Here is a
# reminder of three important characteristics of discrete probability
# distributions.
#
# * For all values on the x-axis, the y value is greater than or equal to 0.
# * For each x, the probability p(x) is equal to the y value
# * The sum of all y values is 1
#
# It looks like this visualization violates the second and third criteria.  The
# sum of the y-values is 2000 not 1.  And the y values represent counts not
# probability.

# # Exercise: Calculate a Discrete Probability Distribution
#
# How can you convert the data into a probability distribution?  Currently, the
# sum of all the y-values is 2000, but the sum needs to equal 1.
#
# What happens if you divide each y-value by the total count of 2000?
#
# Like 54/2000, 111/2000, 163/2000, etc.?
#
# It turns out that for discrete variables, dividing each y-value by the total
# count will give you a discrete probability distribution.  Dividing each value
# by the total is called normalization.
#
# In this exercise, you'll use a for loop to divide each value in your list by
# the total count.  You'll put the results in a new list called
# discrete_probability.
#
# Here is some example code to give you an idea of how to create the new list
# that will hold the normalized counts:
#
# ```python
#
# # a python list
# mylist = [1, 2, 3, 4, 5]
#
# # an empty python list
# newlist = []
#
# # for loop
# for i in range(len(mylist)):
#     newlist.append(mylist[i])
# ```

# In[ ]:


###
# INSTRUCTIONS: Use a for loop to iterate through the
#      count_data list
#
# For each value in the list, divide the value by the total_count
# variable.
#
# You will need to append the results to a new list
#
###
normalized_counts = []

# TODO: Write a for loop to iterate through the count_data list.
#       Use the for loop example given previously to help
#       get yourself started
for data in count_data:
    normalized_counts.append(data / total_count)
    # TODO: Inside the for loop, divide each value in
    # count_data by the total_count variable and append
    # the result to the normalized_counts variable.
print('Here are the normalized counts: ')
print(normalized_counts)


# # Demo: Plot Your Results
#
# We have written code for you that will plot your results.  Run the cell below
# to see the plot.  If you've normalized the counts correctly, your output
# should look like this plot
#
# ![Probability Plot](plot.png)
#

# In[ ]:
import plot
## import matplotlib.pyplot as plt
## plt.bar(count_data, normalized_counts, bottom=0, align='edge', alpha=0.5)
## plt.show()
plot.plot_probability(normalized_counts)


# # Check your Results
#
# Run the code below to check your results.  If the code cell prints out
# "Awesome work!", then your results were what we expected.  We've also
# provided answer code in the next part of the lesson.

# In[ ]:
assert count_data == [54, 111, 163, 222, 277, 336, 276, 220, 171, 111, 59], "The count_data variable is not correct."
assert total_count == 2000, "The total_count variable is not correct."
assert normalized_counts == [54 / 2000, 111 / 2000, 163 / 2000, 222 / 2000, 277 / 2000, 336 / 2000, 276 / 2000, 220 / 2000, 171 / 2000, 111 / 2000, 59 / 2000], "The normalized_count variable is not correct."
print('Awesome work! Your answers are what we expected.')


