import numpy as np
import cv2

input_image = cv2.imread("./images/input.jpg")

cv2.imshow("Original Image",input_image)

cv2.waitKey()

cv2.destroyAllWindows()

up_scaled = cv2.pyrUp(input_image)

cv2.imshow("Up Scaled ", up_scaled)

cv2.waitKey()

cv2.destroyAllWindows()