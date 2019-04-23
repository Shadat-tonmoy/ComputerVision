import numpy as np
import cv2

brightness_factor = 75

input_image = cv2.imread("./images/input.jpg")

cv2.imshow("Original Image", input_image)

brightness_matrix = np.ones(input_image.shape, dtype="uint8") * brightness_factor

manipulated_image = np.add(input_image, brightness_matrix)

cv2.imshow("Brighten Image ", manipulated_image)

cv2.waitKey()

cv2.destroyAllWindows()

