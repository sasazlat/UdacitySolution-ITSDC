
# coding: utf-8

# # Predict state
#
# Here is the current implementation of the `predict_state` function.  It takes
# in a state (a Python list), and then separates those into position and
# velocity to calculate a new, predicted state.  It uses a constant velocity
# motion model.
#
# **In this exercise, we'll be improving this function, and using matrix
# multiplication to efficiently calculate the predicted state!**

# In[1]:


# The current predict state function
# Predicts the next state based on a motion model
def predict_state(state, dt):
    # Assumes a valid state had been passed in
    x = state[0]
    velocity = state[1]
    
    # Assumes a constant velocity model
    new_x = x + velocity * dt
    
    # Create and return the new, predicted state
    predicted_state = [new_x, velocity]
    return predicted_state


# ## Matrix operations
#
# You've been given a matrix class that can create new matrices and performs
# one operation: multiplication.  In our directory this is called `matrix.py`.
#
# Similar to the Car class, we can use this to initialize matrix objects.

# In[2]:


# import the matrix file
import matrix

# Initialize a state vector
initial_position = 0 # meters
velocity = 50 # m/s

# Notice the syntax for creating a state column vector ([ [x], [v] ])
# Commas separate these items into rows and brackets into columns
initial_state = matrix.Matrix([[initial_position], 
                                [velocity]])


# ### Transformation matrix
#
# Next, define the state transformation matrix and print it out!

# In[3]:


# Define the state transformation matrix
dt = 1
tx_matrix = matrix.Matrix([[1, dt], 
                            [0, 1]])

print(tx_matrix)


# ### TODO: Modify the predict state function to use matrix multiplication
#
# Now that you know how to create matrices, modify the `predict_state` function
# to work with them!
#
# Note: you can multiply a matrix A by a matrix B by writing `A*B` and it will
# return a new matrix.
#

# In[ ]:


# The current predict state function
def predict_state_mtx(state, dt):
    ## TODO: Assume that the state passed in is a Matrix object
    ## Using a constant velocity model and a transformation matrix
    ## Create and return the new, predicted state!
    #predicted_state = 0
    x = state[0]
    v = state[1]
    tx_matrix = matrix.Matrix([[1, dt],
                               [0, 1]])
    predicted_state = tx_matrix * state
    return predicted_state


# ### Test cell
#
# Here is an initial state vector and dt to test your function with!

# In[ ]:


# initial state variables
initial_position = 10 # meters
velocity = 30 # m/s

# Initial state vector
initial_state = matrix.Matrix([[initial_position], 
                                [velocity]])


print('The initial state is: ' + str(initial_state))


# after 2 seconds make a prediction using the new function
state_est1 = predict_state_mtx(initial_state, 2)

print('State after 2 seconds is: ' + str(state_est1))


# In[ ]:


# Make more predictions!

# after 3 more
state_est2 = predict_state_mtx(state_est1, 3)

print('State after 3 more seconds is: ' + str(state_est2))

# after 3 more
state_est3 = predict_state_mtx(state_est2, 3)

print('Final state after 3 more seconds is: ' + str(state_est3))


