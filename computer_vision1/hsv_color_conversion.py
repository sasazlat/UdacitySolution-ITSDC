import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image
image = mpimg.imread("images/car_green_screen2.jpg")
plt.imshow(image)
#plt.show()

#Color boundaries
lower_green = np.array([0,200,0])
upper_green = np.array([100,255,100])

#Create a mask area
mask = cv2.inRange(image, lower_green, upper_green)
plt.imshow(mask)
#plt.show()

#Mask the image to let the car show through
masked_image = np.copy(image)
masked_image[mask != 0] = [0,0,0] 
plt.imshow(masked_image)
#plt.show()


#convert image to HSV color space
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
# Convert to HSV
#hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('H channel')
ax1.imshow(h, cmap='gray')
ax2.set_title('S channel')
ax2.imshow(s, cmap='gray')
ax3.set_title('V channel')
ax3.imshow(v, cmap='gray')
#plt.show()


lower_green_hsv = np.array([50,100,40])
upper_green_hsv = np.array([70,255,255])
hsv_mask = cv2.inRange(hsv, lower_green_hsv, upper_green_hsv)


## TODO: Define the masked area and mask the image
plt.imshow(hsv_mask)
plt.show()
hsv_masked_image = np.copy(image)
hsv_masked_image[hsv_mask != 0] = [0,0,0]
# Don't forget to make a copy of the original image to manipulate
plt.imshow(hsv_masked_image)
plt.show()

#green = np.uint8([[[0,100,0 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#print (hsv_green)
print('Image dimensions:', image.shape)

background_image = mpimg.imread('images/sky (1).jpg')
background_image_copy = np.copy(background_image)
print (background_image_copy.shape)
plt.imshow(background_image_copy)
plt.show()
background_image_resized = cv2.resize(background_image_copy, (660, 450))
plt.imshow(background_image_resized)
plt.show()

background_image_resized[hsv_mask == 0] = [0, 0, 0]
## TODO: Display the background and make sure 
plt.imshow(background_image_resized)
plt.show()

complete_image = hsv_masked_image + background_image_resized
plt.imshow(complete_image)
plt.show()
