import numpy as np
import cv2

input_image = cv2.imread("./images/input.jpg")

cv2.imshow("Original Image",input_image)

cv2.waitKey()

cv2.destroyAllWindows()

resized_image = cv2.resize(input_image,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Resized Image", resized_image)

cv2.waitKey()

cv2.destroyAllWindows()
