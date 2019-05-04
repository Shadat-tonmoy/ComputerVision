import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/Origin_of_Species.jpg")

gray_image = openCV.cvtColor(input_image, openCV.COLOR_BGR2GRAY)

blurred_image = openCV.GaussianBlur(gray_image, (3, 3), 0)

threshold_image = openCV.adaptiveThreshold(blurred_image, 255, openCV.ADAPTIVE_THRESH_GAUSSIAN_C, openCV.THRESH_BINARY,
                                           3, 3)

openCV.imshow("Threshold Image", threshold_image)

openCV.waitKey()

openCV.destroyAllWindows()

_, threshold_image = openCV.threshold(blurred_image, 0, 255, openCV.THRESH_BINARY + openCV.THRESH_OTSU)

openCV.imshow("Threshold Image", threshold_image)

openCV.waitKey()

openCV.destroyAllWindows()
