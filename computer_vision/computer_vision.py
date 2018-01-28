import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

image = mpimg.imread("images/sky.jpg")
pixel_value = image[10,34]
dimensuin = image.shape[0]
gray_scale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_scale,cmap='gray')
print (pixel_value)
pixel_value = gray_scale[10,34]
print (pixel_value)