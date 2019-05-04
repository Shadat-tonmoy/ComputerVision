import numpy as np
import cv2

input = cv2.imread('./images/input.jpg')        # reading original image from directory

# input = cv2.imread('./images/input.jpg',0)    # convert to gray scale while loading the image

cv2.imshow('Original Image', input)             # showing original image

cv2.waitKey()                                   # waiting for any key to be pressed

gray_scaled_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)      # converting original image to gray scale image using cvtColor

cv2.imshow('Gray Scaled Image',gray_scaled_image)                # showing gray scale image

cv2.waitKey()                                                    # waiting for any key to be pressed

cv2.destroyAllWindows()                                          # close all opened window





