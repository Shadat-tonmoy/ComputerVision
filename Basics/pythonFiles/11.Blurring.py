import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/elephant.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

blurring_kernel_3x3 = np.ones((3, 3), np.float32) / 9

'''
kernel is a nxn dimension matrix which is normalized by nxn. normalization is done by dividing all the element by n*n 
so that the sum of all elements are 1. Example of Kernel of 3x3 

1/9 * 
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
'''

blurred_image = openCV.filter2D(input_image, -1, blurring_kernel_3x3)   # apply blurring effect with filter2D function

openCV.imshow("Blurred Image", blurred_image)

openCV.waitKey()

blurring_kernel_7x7 = np.ones((7, 7), np.float32) / 49


blurred_image = openCV.filter2D(input_image, -1, blurring_kernel_7x7)

openCV.imshow("Blurred Image with 7x7", blurred_image)

openCV.waitKey()

openCV.destroyAllWindows()





