

# coding: utf-8

# # Why use numpy arrays?
# Numpy is one of those tools that will keep showing up as you learn about self
# driving cars.  This is because numpy arrays tend to be:
#
# 1.  **compact** (they don't take up as much space in memory as a Python
# list).
#
# 2.  **efficient** (computations usually run quicker on numpy arrays then
# Python lists).
#
# 3.  **convenient** (which we'll talk about more now).

# In[ ]:


# consider this 2d python grid (list of lists)
grid = [[0, 1, 5],
    [1, 2, 6],
    [2, 3, 7],
    [3, 4, 8]]

# It's easy to print, for example, row number 0:
print(grid[0])


# In[ ]:


# but how would you print COLUMN 0?  In numpy, this is easy
import numpy as np

np_grid = np.array([[0, 1, 5],
    [1, 2, 6],
    [2, 3, 7],
    [3, 4, 8]])

# The ':' usually means "*all values*
print(np_grid[:,0])


# In[ ]:


# What if you wanted to change the shape of the array?

# For example, we can turn the 2D grid from above into a 1D array
# Here, the -1 means automatically fit all values into this 1D shape
np_1D = np.reshape(np_grid, (1, -1))

print(np_1D)


# In[ ]:


# We can also create a 2D array of zeros or ones
# which is useful for car world creation and analysis

# Create a 5x4 array
zero_grid = np.zeros((5, 4))
eye_grid = np.eye((5))

print(zero_grid)
print(eye_grid)


