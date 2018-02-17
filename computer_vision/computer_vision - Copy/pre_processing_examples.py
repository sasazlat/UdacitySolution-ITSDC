
# coding: utf-8

# # Cropping and Resizing

# ### Import resources

# In[ ]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

#get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read in the first image of a stop sign

# In[ ]:


# Read in the image
stop1 = mpimg.imread('images/stop_sign.jpg')

print('Image shape: ', stop1.shape)
plt.imshow(stop1)
plt.show()


# ### Read in the second image

# In[ ]:


# Read in the image
stop2 = mpimg.imread('images/stop_sign2.jpg')

print('Image shape: ', stop2.shape)
plt.imshow(stop2)
plt.show()


# ## Crop this image so that it resembles the first image

# In[ ]:


# To crop and image, you can use image slicing
# which is just slicing off a portion of the image array

# Make a copy of the image to manipulate
image_crop = np.copy(stop2)

# Define how many pixels to slice off the sides of the original image
row_crop = 90
col_crop = 250

# Using image slicing, subtract the row_crop from top/bottom and col_crop from
# left/right
image_crop = stop2[row_crop:-row_crop, col_crop:-col_crop, :]

plt.imshow(image_crop)
plt.show()


# ## Resize the cropped image to be the same as the first
#
# Recall that the shape of the first image is `(1500, 1389, 3)`.
#

# In[ ]:


# Use OpenCV's resize function
standardized_im = cv2.resize(image_crop, (1389, 1500))

print('Image shape: ', standardized_im.shape)

# Plot the two images side by side
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
ax1.set_title('Stop sign 1')
ax1.imshow(stop1)
ax2.set_title('Standardized stop sign 2')
ax2.imshow(standardized_im)
plt.show()


# ## Compare these images
#
# Now you should be able to compare these images pixel by pixel!
# We'll add up the red channel values in each image, and they should be fairly
# close, which means we can use this similarity to characterize these images.
#
# For comparison, we'll also show what happens when you perform this comparison
# using the orginal `stop_sign2.jpg`.

# In[ ]:


# Sum all the red channel values and compare
red_sum1 = np.sum(stop1[:,:,0])
red_sum2 = np.sum(standardized_im[:,:,0])

print('Sum of all red pixel values in the first stop sign image: ', red_sum1)
print('Sum of red pixel values in the second, standardized image: ', red_sum2)

red_sum_orig = np.sum(stop2[:,:,0])

print('\nFor comparison, the sum of red pixels in the non-standardized image: ', red_sum_orig)


# In[ ]:


## Note: you have been given two other images:
# `yield.jpg` and `walk.jpg`
# You can look at these images and see what kind of RGB values might distinguish them

yield_image = mpimg.imread("images/yield.jpg")
walk_image = mpimg.imread("images/walk.jpg")
print ("Size of yield_image is ", yield_image.shape)
print ("Size of walk_image is ", walk_image.shape)
plt.imshow(yield_image)
plt.show()
plt.imshow(walk_image)
plt.show()

yield_crop = yield_image[100:-300, 300:-300]
print ("Size of yield_crop is ", yield_crop.shape)
plt.imshow(yield_crop)
plt.show()

walk_copy = np.copy(walk_image)
walk_copy = walk_copy[:, 60:-60]
print ("Size of walk_copy is ", walk_copy.shape)
plt.imshow(walk_copy)
plt.show()
walk_standardize = cv2.resize(walk_copy, (424,284))


f1, (ax3, ax4) = plt.subplots(1,2,figsize=(20,10))
ax3.set_title('Pictire yield')
ax3.imshow(yield_crop)
ax4.set_title('Picture walk')
ax4.imshow(walk_standardize)
plt.show()