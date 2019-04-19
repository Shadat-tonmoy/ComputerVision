import numpy as np
import cv2

input_image = cv2.imread("./images/Trump.jpg")

width, height = input_image.shape[:2]

cv2.imshow("Trump", input_image)

cv2.waitKey()

cv2.destroyAllWindows()

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(input_image, rotation_matrix, (width, height))

cv2.imshow("Rotated Trump", rotated_image)

cv2.waitKey()

cv2.destroyAllWindows()

transposed_rotation = cv2.transpose(input_image)

cv2.imshow("Transposed Rotation ",transposed_rotation)

cv2.waitKey()

cv2.destroyAllWindows()