import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
img = mpimg.imread("images\\circles.png", 1)
plt.imshow(img)
plt.show()

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
lower_range = np.array([169, 100, 100], dtype=np.uint8)
upper_range = np.array([189, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_range, upper_range)
 
cv2.imshow('mask',mask)
cv2.imshow('image', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
 
while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
 
cv2.destroyAllWindows()
