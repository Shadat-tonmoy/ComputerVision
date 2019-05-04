import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/elephant.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

'''
GaussianBlur apply a kernel of nxn size called Gaussian Kernel to blur image. Its almost same as kernel blurring 

'''

blurred_image = openCV.GaussianBlur(input_image, (7, 7), 0)

openCV.imshow("Blurred Image", blurred_image)

openCV.waitKey()

openCV.destroyAllWindows()