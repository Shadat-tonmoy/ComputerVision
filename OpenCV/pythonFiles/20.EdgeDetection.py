import numpy as np
import cv2 as openCV


'''
Edges in image is defined by sudden changes in an image and they can encode just as much information as pixels
There are different edge detection algorithm out there.

Sobel - to emphasize vertical or horizontal edges
Laplacian - Gets all orientation
Canny - Optimal and best in performance and accuracy

Canny Edge Detection algorithm -
01. Apply Gaussian Blurring
02. Finds intensity gradients of the image
03. Removes pixels that are not edges (Applying non-maximum suppression)
04. Apply thresholds (If pixel is within the upper and lower thresholds,it is considered as an edge.Known as hysteresis)
'''

input_image = openCV.imread("./images/input.jpg",0)

openCV.imshow("Original Image", input_image)

openCV.waitKey()

openCV.destroyAllWindows()

# sobel_x = openCV.Sobel(input_image, openCV.CV_64F, 0, 1, ksize=5)
#
# sobel_y = openCV.Sobel(input_image, openCV.CV_64F, 1, 0, ksize=5)
#
# sobel_OR = openCV.bitwise_or(sobel_x, sobel_y)
#
# openCV.imshow("Sobel X", sobel_x)
#
# openCV.waitKey()
#
# openCV.imshow("Sobel Y", sobel_x)
#
# openCV.waitKey()
#
# openCV.imshow("Sobel OR", sobel_OR)
#
# openCV.waitKey()
#
# openCV.destroyAllWindows()
#
# laplacian = openCV.Laplacian(input_image, openCV.CV_64F)
#
# openCV.imshow("Laplacian", laplacian)
#
# openCV.waitKey()
#
# openCV.destroyAllWindows()

'''
Canny is widely used in computer vision. Using opencv we need to pass 2 parameters threshold1 and threshold2
Any gradient value larger than threshold2 is considered to be an edge 
Any gradient value below threshold1 is considered not to be an edge
'''

canny_edge = openCV.Canny(input_image, 10, 160)

openCV.imshow("Canny", canny_edge)

openCV.waitKey()

openCV.destroyAllWindows()





