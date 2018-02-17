
# coding: utf-8

# # Day and Night Image Classifier
# ---
#
# The day/night image dataset consists of 200 RGB color images in two
# categories: day and night.  There are equal numbers of each example: 100 day
# images and 100 night images.
#
# We'd like to build a classifier that can accurately label these images as day
# or night, and that relies on finding distinguishing features between the two
# types of images!
#
# *Note: All images come from the [AMOS
# dataset](http://cs.uky.edu/~jacobs/datasets/amos/) (Archive of Many Outdoor
# Scenes).*
#

# ### Import resources
#
# Before you get started on the project code, import the libraries and
# resources that you'll need.

# In[ ]:

import cv2 # computer vision library
import helpers

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Training and Testing Data
# The 200 day/night images are separated into training and testing datasets.
#
# * 60% of these images are training images, for you to use as you create a
# classifier.
# * 40% are test images, which will be used to test the accuracy of your
# classifier.
#
# First, we set some variables to keep track of some where our images are
# stored:
#
#     image_dir_training: the directory where our training image data is stored
#     image_dir_test: the directory where our test image data is stored

# In[ ]:


# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"


# ## Load the datasets
#
# These first few lines of code will load the training day/night images and
# store all of them in a variable, `IMAGE_LIST`.  This list contains the images
# and their associated label ("day" or "night").
#
# For example, the first image-label pair in `IMAGE_LIST` can be accessed by
# index:
# ``` IMAGE_LIST[0][:]```.
#

# In[ ]:


# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(image_dir_training)


# ---
# # 1.  Visualize the input images
#

# In[ ]:


# Select an image and its label by list index
image_index = 0
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]

## TODO: Print out 1. The shape of the image and 2. The image's label `selected_label`

## TODO: Display a night image
# Note the differences between the day and night images
# Any measurable differences can be used to classify these images


