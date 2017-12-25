
# coding: utf-8

# # Vectors in Python
#
# In the following exercises, you will work on coding vectors in Python.
#
# Assume that you have a state vector
# $$\mathbf{x_0}$$
#
# representing the x position, y position, velocity in the x direction, and
# velocity in the y direction of a car that is driving in front of your
# vehicle.  You are tracking the other vehicle.
#
# Currently, the other vehicle is 5 meters ahead of you along your x-axis, 2
# meters to your left along your y-axis, driving 10 m/s in the x direction and
# 0 m/s in the y-direction.  How would you represent this in a Python list
# where the vector contains `<x, y, vx, vy>` in exactly that order?
#
#
# ### Vector Assignment: Example 1

# In[ ]:


## Practice working with Python vectors

## TODO: Assume the state vector contains values for <x, y, vx, vy>
## Currently, x = 5, y = 2, vx = 10, vy = 0
## Represent this information in a list
x0 = [5,2,10,0]

# ### Test your code
#
# Run the cell below to test your code.
#
# The test code uses a Python assert statement.  If you have a code statement
# that resolves to either True or False, an assert statement will either:
# * do nothing if the statement is True
# * throw an error if the statement is False
#
#
# A Python assert statement
# will output an error if the answer was not as expected.  If the
# answer was as expected, then nothing will be outputted.

# In[ ]:


### Test Cases
### Run these test cases to see if your results are as expected
### Running this cell should produce no output if all assertions are True
assert x0 == [5, 2, 10, 0]


# ### Vector Assignment: Example 2
#
# The vehicle ahead of you has now moved farther away from you.  You know that
# the vehicle has moved 3 meters forward in the x-direction, 5 meters forward
# in the y-direction, has increased its x velocity by 2 m/s and has increased
# its y velocity by 5 m/s.
#
# Store the change in position and velocity in a list variable called xdelta

# In[ ]:


## TODO: Assign the change in position and velocity to the variable
## xdelta.  Remember that the order of the vector is x, y, vx, vy
xdelta = [3,5,2,5]


# In[ ]:


### Test Case
### Run this test case to see if your results are as expected
### Running this cell should produce no output if all assertions are True
assert xdelta == [3, 5, 2, 5]


# ### Vector Math: Addition
#
# Calculate the tracked vehicle's new position and velocity.  Here are the
# steps you need to carry this out:
#
# * initialize an empty list called x1
# * add xdelta to x0 using a for loop
# * store your results in x1 as you iterate through the for loop using the
# append method

# In[ ]:


## TODO: Add the vectors together element-wise.  For example,
## element-wise addition of [2, 6] and [10, 3] is [12, 9].
## Place the answer in the x1 variable.
##
## Hint: You can use a for loop.  The append method might also
## be helpful.
x1 = [8,7,12,5]


# In[ ]:


### Test Case
### Run this test case to see if your results are as expected
### Running this cell should produce no output if all assertions are True
assert x1 == [8, 7, 12, 5]


# ### Vector Math: Scalar Multiplication
#
# You have your current position in meters and current velocity in meters per
# second.  But you need to report your results at a company meeting where most
# people will only be familiar with working in feet rather than meters.
# Convert your position vector x1 to feet and feet/second.
#
# This will involve scalar multiplication.  The process for coding scalar
# multiplication is very similar to vector addition.  You will need to:
# * initialize an empty list
# * use a for loop to access each element in the vector
# * multiply each element by the scalar
# * append the result to the empty list

# In[ ]:


## TODO: Multiply each element in the x1 vector by the conversion
## factor shown belowand store the results in the variable s.
## Use a for loop
meters_to_feet = 1.0 / 0.3048
x1feet = [8 * meters_to_feet,7 * meters_to_feet,12 * meters_to_feet,5 * meters_to_feet]


# In[ ]:


### Test Cases
### Run this test case to see if your results are as expected
### Running this cell should produce no output if all assertions are True
x1feet_sol = [8 / .3048, 7 / .3048, 12 / .3048, 5 / .3048]

assert(len(x1feet) == len(x1feet_sol)) 
for response, expected in zip(x1feet, x1feet_sol):
    assert(abs(response - expected) < 0.001)


# ### Vector Math: Dot Product
#
# The tracked vehicle is currently at the state represented by
# $$\mathbf{x_1} = [8, 7, 12, 5] $$.
#
# Where will the vehicle be in two seconds?
#
# You could actually solve this problem very quickly using Matrix
# multiplication, but we have not covered that yet.  Instead, think about the
# x-direction and y-direction separately and how you could do this with the dot
# product.
#
# #### Solving with the Dot Product
# You know that the tracked vehicle at x1 is 8m ahead of you in the x-direction
# and traveling at 12m/s.  Assuming constant velocity, the new x-position after
# 2 seconds would be
#
# $$8 + 12*2 = 32$$
#
# The new y-position would be
# $$7 + 5*2 = 17$$
#
# You could actually solve each of these equations using the dot product:
#
# $$x_2 = [8, 7, 12, 5]\cdot[1, 0, 2, 0] \\\
# = 8\times1 + 7\times0 + 12\times2 + 5\times0 \\\
# = 32$$
#
# $$y_2 = [8, 7, 12, 5]\cdot[0, 1, 0, 2] \\\
# = 8\times0 + 7\times1 + 12\times0 + 5\times2 \\\
# = 17$$
#
# Since you are assuming constant velocity, the final state vector would be
#
# $$\mathbf{x_2} = [32, 17, 12, 5]$$
#
# #### Coding the Dot Product
#
# Now, calculate the state vector $$\mathbf{x_2}$$ but with code.  You will
# need to calculate the dot product of two vectors.  Rather than writing the
# dot product code for the x-direction and then copying the code for the
# y-direction, write a function that calculates the dot product of two Python
# lists.
#
# Here is an outline of the steps:
# * initialize an empty list
# * initialize a variable with value zero to accumulate the sum
# * use a for loop to iterate through the vectors.  Assume the two vectors have
# the same length
# * accumulate the sum as you multiply elements together
#
# You will see in the starter code that x2 is already being calculated for you
# based on the results of your dotproduct function

# In[ ]:


## TODO: Fill in the dotproduct() function to calculate the
## dot product of two vectors.
##

## Here are the inputs and outputs of the dotproduct() function:
##     INPUTS: vector, vector
##     OUTPUT: dot product of the two vectors
##
##
## The dot product involves mutliplying the vectors element
## by element and then taking the sum of the results
##
## For example, the dot product of [9, 7, 5] and [2, 3, 4] is
## 9*2+7*3 +5*4 = 59
##
## Hint: You can use a for loop.  You will also need to accumulate
## the sum as you iterate through the vectors.  In Python, you can accumulate
## sums with syntax like w = w + 1
x2 = []

def dotproduct(vectora, vectorb):
    
    # variable for accumulating the sum
    result = 0
    
    # TODO: Use a for loop to multiply the two vectors
    # element by element.  Accumulate the sum in the result variable
    lena = len(vectora)
    for i in range(lena):
        result = result + vectora[i] * vectorb[i]    
    
    return result
    
x2 = [dotproduct([8, 7, 12, 5], [1, 0, 2, 0]), 
      dotproduct([8, 7, 12, 5], [0, 1, 0, 2]),
      12,
      5]


# In[ ]:


### Test Case
### Run this test case to see if your results are as expected
### Running this cell should produce no output if all assertions are True
assert x2 == [32, 17, 12, 5]


