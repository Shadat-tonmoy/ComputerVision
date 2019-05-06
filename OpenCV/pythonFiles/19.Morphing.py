import numpy as np
import cv2 as openCV

'''
Morphing can be divided into several operation like dilation, erosion, opening, closing

Dilation - Adds pixels to the boundaries of object in image
Erosion - Removes pixels at the boundaries  of object in image
Opening - Erosion followed by dilation
Closing - Dilation followed by erosion
'''


input_image = openCV.imread("./images/opencv_inv.png")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

kernel_matrix = np.ones((3, 3), np.float32)

dilated_image = openCV.dilate(input_image, kernel_matrix, iterations=1)

openCV.imshow("Dilated Image", dilated_image)

openCV.waitKey()

eroded_image = openCV.erode(input_image, kernel_matrix, iterations=1)

openCV.imshow("Eroded Image", eroded_image)

openCV.waitKey()

opened_image = openCV.morphologyEx(input_image, openCV.MORPH_OPEN, kernel_matrix, iterations=1)

openCV.imshow("Opened Image", opened_image)

openCV.waitKey()

closed_image = openCV.morphologyEx(input_image, openCV.MORPH_CLOSE, kernel_matrix, iterations=1)

openCV.imshow("Closed Image", closed_image)

openCV.waitKey()

openCV.destroyAllWindows()