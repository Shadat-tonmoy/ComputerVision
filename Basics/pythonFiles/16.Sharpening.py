import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/input.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

kernel_matrix = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])

sharpen_image = openCV.filter2D(input_image, -1, kernel_matrix)

openCV.imshow("Sharpen Image", sharpen_image)

openCV.waitKey()

openCV.destroyAllWindows()