import cv2 as openCV
import numpy as np


input_image = openCV.imread("./images/elephant.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

blurred_image = openCV.blur(input_image, (3, 3))

'''
box filter works by averaging all the surrounding pixels. This takes the pixels under the box and replaces the central
element. 
'''

openCV.imshow("Blurred Image", blurred_image)

openCV.waitKey()

openCV.destroyAllWindows()