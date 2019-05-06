import numpy as np
import cv2

input = cv2.imread('./images/input.jpg')

cv2.imshow("Original Image", input)

cv2.waitKey()

cv2.destroyAllWindows()

height, width = input.shape[:2]

tx, ty = width/4, height/4

transformation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

transformed_image = cv2.warpAffine(input, transformation_matrix, (width, height))

cv2.imshow("Transformed Image ", transformed_image)

cv2.waitKey()

cv2.destroyAllWindows()

