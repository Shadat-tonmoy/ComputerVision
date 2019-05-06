import numpy as np
import cv2 as openCV


input = openCV.imread('./images/input.jpg')

print(input.shape)

print(type(input))

openCV.imshow('Test Image', input)

openCV.waitKey(0)

openCV.destroyAllWindows()



