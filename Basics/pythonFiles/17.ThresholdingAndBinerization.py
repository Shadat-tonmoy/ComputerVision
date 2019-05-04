import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/Origin_of_Species.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

gray_scaled_image = openCV.cvtColor(input_image, openCV.COLOR_BGR2GRAY)

openCV.imshow("Gray Scaled", gray_scaled_image)

openCV.waitKey()

ret, threshold_image = openCV.threshold(gray_scaled_image, 127, 255, openCV.THRESH_BINARY)

openCV.imshow("Threshold Image", threshold_image)

openCV.waitKey()

openCV.destroyAllWindows()