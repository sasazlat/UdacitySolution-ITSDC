import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image
image = mpimg.imread("images/car_green_screen2.jpg")
plt.imshow(image)
plt.show()

#Color boundaries
lower_green = np.array([0,200,0])
upper_green = np.array([100,255,100])

#Create a mask area
mask = cv2.inRange(image, lower_green, upper_green)
plt.imshow(mask)
plt.show()

#Mask the image to let the car show through
masked_image = np.copy(image)
masked_image[mask != 0] = [0,0,0] 
plt.imshow(masked_image)
plt.show()


#convert image to HSV color space
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
