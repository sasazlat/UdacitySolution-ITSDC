
# coding: utf-8

# # Plotting Position vs Time
# In this notebook you will plot a position vs time graph of the data you just
# saw.
#
# First, I will demonstrate such a plot by following these steps:
#
# 1.  Importing `pyplot`, Python's most popular plotting library.
# 2.  Storing data to be plotted in variables named `X` and `Y`
# 3.  Creating a scatter plot of this data using pyplot's `scatter()` function.
# 4.  Adding a line connecting two data points using pyplot's `plot()`
# function.
# 4.  Adding axis labels and a title to the graph.

# In[ ]:


# Step 1.
#  we import pyplot as plt so we can refer to the pyplot
#  succinctly.  This is a standard convention for this library.
from matplotlib import pyplot as plt


# Initially, I only told you the mileage at 2:00 and 3:00.  The data looked
# like this.
#
# | Time | Odometer <br>(miles) |
# |:----:|:--------------------------------:|
# | 2:00 | 30 |
# | 3:00 | 80 |
#
# I'd like to make a scatter plot of this data and I want my **horizontal**
# axis to show time and my **vertical** axis to show mileage.
#
# In this notebook (and those that follow), we are going to use a capital `X`
# to store horizontal axis data and a capital `Y` to store vertical axis data.
# In this case:

# In[ ]:


# Step 2.
#  get the data into variables called X and Y.  This naming pattern
#  is a convention.  You could use any variables you like.
X = [2,3]
Y = [30,80]


# In[ ]:


# Step 3.
#  create a scatter plot using plt.scatter.  Note that you NEED
#  to call plt.show() to actually see the plot.  Forgetting to
#  call plt.show() is a common source of problems for people
#  new to this library
plt.scatter(X,Y)
plt.show()

