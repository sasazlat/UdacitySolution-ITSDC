import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
img = mpimg.imread("images\\circles.png", 1)
plt.imshow(img)
plt.show()

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
lower_range = np.array([160, 100, 100])
upper_range = np.array([180, 255, 255])
mask = cv2.inRange(hsv, lower_range, upper_range) 
plt.imshow(mask, cmap= 'gray')
plt.show()

#masked image
masked_img = np.copy(img)
masked_img[mask == 0] = [0,0,0]

plt.imshow(masked_img)
plt.show()

gray_img = cv2.cvtColor(masked_img, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_img, cmap="gray")
plt.show()


h,s,v = cv2.split(hsv)
# Visualize the individual color channels
f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(10,5))
ax1.set_title('Image')
ax1.imshow(masked_img, cmap='gray')

ax2.set_title('H channel')
ax2.imshow(h, cmap='gray')

ax3.set_title('S channel')
ax3.imshow(s, cmap='gray')

ax4.set_title('V channel')
ax4.imshow(v, cmap = "gray")
plt.show()

# Create color channel histograms
h_hist = np.histogram(hsv[:,:,0], bins=32, range=(0, 200))
s_hist = np.histogram(hsv[:,:,1], bins=32, range=(0, 180))
v_hist = np.histogram(hsv[:,:,2], bins=32, range=(0, 200))

# Generating bin centers
bin_edges = h_hist[1]
print (bin_edges[0:len(bin_edges)])
bin_centers = (bin_edges[1:]  + bin_edges[0:-1])/2
print (bin_centers)

bin_centers = (bin_edges[1:]  + bin_edges[0:-1])/2
fig = plt.figure(figsize=(12,3))
plt.subplot(131)
plt.bar(bin_centers, h_hist[0])
plt.xlim(0, 200)
plt.title('H Histogram')
plt.subplot(132)
plt.bar(bin_centers, s_hist[0])
plt.xlim(0, 180)
plt.title('S Histogram')
plt.subplot(133)
plt.bar(bin_centers, v_hist[0])
plt.xlim(0, 200)
plt.title('V Histogram')
plt.show()

# 3x3 array for edge detection
high_pass = np.array([[0, -1, 0], 
                   [-1, 4, -1], 
                   [0, -1, 0]])

filtered_img = cv2.filter2D(gray_img, -1, high_pass)
plt.imshow(filtered_img, cmap="gray")
plt.show()