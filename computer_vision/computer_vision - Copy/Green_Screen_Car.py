
# coding: utf-8

# # Color Masking, Green Screen

# ### Import resources

# In[10]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

#get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read in and display the image

# In[5]:


# Read in the image
image = mpimg.imread('images/car_green_screen.jpg')


# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)


# Display the image
plt.imshow(image)
plt.show()




# ### Define the color threshold

# In[13]:


# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])


# ### Create a mask

# In[15]:


# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Vizualize the mask
plt.imshow(mask, cmap='gray')
mask
plt.show()


# In[16]:


# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)
plt.show()


# ## TODO: Mask and add a background image

# In[ ]:


# Load in a background image, and convert it to RGB
background_image = mpimg.imread('images/sky (1).jpg')

## TODO: Crop it or resize the background to be the right size (450x660)
background_image_copy = np.copy(background_image)
print (background_image_copy.shape)
plt.imshow(background_image_copy)
plt.show()
background_image_resized = cv2.resize(background_image_copy, (660, 450))
plt.imshow(background_image_resized)
plt.show()


## TODO: Mask the cropped background so that the pizza area is blocked
# Hint mask the opposite area of the previous image
background_image_resized[mask == 0] = [0, 0, 0]
## TODO: Display the background and make sure 
plt.imshow(background_image_resized)
plt.show()

# ### TODO:  Create a complete image

# In[ ]:


## TODO: Add the two images together to create a complete image!
# complete_image = masked_image + crop_background
complete_image = masked_image + background_image_resized
plt.imshow(complete_image)
plt.show()