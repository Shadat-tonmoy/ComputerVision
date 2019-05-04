import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/elephant.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

median_blurred_image = openCV.medianBlur(input_image, 7)

openCV.imshow("Blurred Image", median_blurred_image)

openCV.waitKey()

bilateral_blurring = openCV.bilateralFilter(input_image, 9, 75, 75)

openCV.imshow("Bilateral Blurred Image", bilateral_blurring)

openCV.waitKey()

openCV.destroyAllWindows()