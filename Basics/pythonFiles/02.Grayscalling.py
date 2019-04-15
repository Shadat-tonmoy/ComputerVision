import numpy as np
import cv2

input = cv2.imread('./images/input.jpg')

# input = cv2.imread('./images/input.jpg',0)  # convert to gray scale while loading the image

cv2.imshow('Original Image',input)

cv2.waitKey()

gray_scaled_image = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Scaled Image',gray_scaled_image)

cv2.waitKey()

cv2.destroyAllWindows()





