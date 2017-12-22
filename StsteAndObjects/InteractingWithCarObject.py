
# coding: utf-8

# # Interacting with a Car Object

# In this notebook, you've been given some of the starting code for creating
# and interacting with a car object.
#
# Your tasks are to:
# 1.  Become familiar with this code.
#     - Know how to create a car object, and how to move and turn that car.
# 2.  Constantly visualize.
#     - To make sure your code is working as expected, frequently call
#     `display_world()` to see the result!
# 3.  **Make the car move in a 4x4 square path.**
#     - If you understand the move and turn functions, you should be able to
#     tell a car to move in a square path.  This task is a **TODO** at the end
#     of this notebook.
#
# Feel free to change the values of initial variables and add functions as you
# see fit!
#
# And remember, to run a cell in the notebook, press `Shift+Enter`.

# In[1]:
import numpy as np
import car1 as car
import color1

#get_ipython().run_line_magic('matplotlib', 'inline')


# ### Define the initial variables

# In[2]:


# Create a 2D world of 0's
height = 4
width = 6
world = np.zeros((height, width))

# Define the initial car state
initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)


# ### Create a car object

# In[3]:


# Create a car object with these initial params
carla = car.Car(initial_position, velocity, world)

print('Carla\'s initial state is: ' + str(carla.state))

carla.display_world()

# ### Move and track state

# In[4]:


# Move in the direction of the initial velocity
carla.move()

# Track the change in state
print('Carla\'s state is: ' + str(carla.state))

# Display the world
carla.display_world()


# ## TODO: Move in a square path
# 
# Using the `move()` and `turn_left()` functions, make carla traverse a 4x4 square path.
# 
# The output should look like:
# <img src="files/4x4_path.png" style="width: 30%;">

# In[ ]:


## TODO: Make carla traverse a 4x4 square path
carla.move()
carla.move()

carla.turn_right()

carla.move()
carla.move()
carla.move()

carla.turn_right()

carla.move()
carla.move()
carla.move()

carla.turn_right()

carla.move()
carla.move()
carla.move()
carla.display_world()

carlo = car.Car([0,2],[1,0],world, 'y')
carlo.display_world()
carlo.display_world()
carlo.move()
carlo.move()
carlo.turn_right()
carlo.display_world()
## Display the result

r = 200
g = 0
b = 200

# Create the color object
test_color = color1.Color(r, g, b)
test_color2 = color1.Color(100, 55, 23)

# This will throw an error if the class code is incomplete
print(test_color + test_color2)