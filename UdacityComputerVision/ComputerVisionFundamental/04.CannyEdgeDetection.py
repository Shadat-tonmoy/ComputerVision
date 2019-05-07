import numpy as np
import matplotlib.image as mpimage
import matplotlib.pyplot as plt
import cv2 as openCV

'''

*** The algorithm will first detect strong edge (strong gradient) pixels above the high_threshold, and reject pixels below
the low_threshold. Next, pixels with values between the low_threshold and high_threshold will be included as long as 
they are connected to strong edges. The output edges is a binary image with white pixels tracing out the detected edges 
and black everywhere else.
 
Using opencv we can call the Canny Algorithm as following...

edges = cv2.Canny(gray, low_threshold, high_threshold)

*** In this case, we are applying Canny to the image gray and our output will be another image called edges. low_threshold 
and high_threshold are our thresholds for edge detection.

What would be the reasonable range for these parameter! 

*** In our case, converting to gray scale has left us with an 8-bit image, so each pixel can take 2^8 = 256 possible values. 
Hence, the pixel values range from 0 to 255.

*** This range implies that derivatives (essentially, the value differences from pixel to pixel) will be on the scale of
tens or hundreds. So, a reasonable range for our threshold parameters would also be in the tens to hundreds.

*** As far as a ratio of low_threshold to high_threshold, John Canny himself recommended a low to high ratio of 
1:2 or 1:3.

'''

image = mpimage.imread("../images/exit-ramp.jpg")

gray_image = openCV.cvtColor(image, openCV.COLOR_BGR2GRAY)

kernel_size = 5

# plt.imshow(gray_image, cmap='gray')

# plt.show()

blurred_image = openCV.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)

low_threshold = 50

high_threshold = 150

detected_edge = openCV.Canny(blurred_image, low_threshold, high_threshold)

plt.imshow(detected_edge, cmap='Greys_r')

plt.show()
