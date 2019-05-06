import cv2 as  openCV
import numpy as np

input_image = openCV.imread("./images/elephant.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

blurred_image = openCV.fastNlMeansDenoisingColored(input_image, None, 6, 6, 7, 21)

openCV.imshow("Blurred Image", blurred_image)

openCV.waitKey()

openCV.destroyAllWindows()