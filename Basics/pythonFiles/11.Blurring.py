import numpy as np
import cv2 as openCV

input_image = openCV.imread("./images/input.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

openCV.destroyAllWindows()



