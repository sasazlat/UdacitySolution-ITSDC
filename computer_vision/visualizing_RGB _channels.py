
# coding: utf-8

# # RGB colorspace

# ### Import resources

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg




# ### Read in an image

# In[2]:


# Read in the image
image = mpimg.imread('images/wa_state_highway.jpg')

plt.imshow(image)
plt.show()


# ### RGB channels
#
# Visualize the levels of each color channel.  Pay close attention to the
# traffic signs!

# In[3]:


# Isolate RGB channels
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('R channel')
ax1.imshow(r, cmap='gray')
ax2.set_title('G channel')
ax2.imshow(g, cmap='gray')
ax3.set_title('B channel')
ax3.imshow(b, cmap='gray')
plt.show()