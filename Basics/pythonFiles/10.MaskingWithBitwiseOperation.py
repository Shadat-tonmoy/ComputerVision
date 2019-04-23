import numpy as np
import cv2


square = np.zeros((300, 300), dtype="uint8")

width, height = square.shape[:2]

rectangle = cv2.rectangle(square.copy(), (50, 50), (250, 250), 255, -1)

cv2.imshow("Square", rectangle)

ellipse = cv2.ellipse(square, (width/2, height/2), (width/2, height/2), 30, 0, 180,color=255)

cv2.imshow("Ellipse", ellipse)

cv2.waitKey()

cv2.destroyAllWindows()


# input_image = cv2.imread("./images/input.jpg")
#
# cv2.imshow("Original Image ", input_image)
#
# cv2.waitKey()
#
# cv2.destroyAllWindows()
#
# rectangle = cv2.rectangle()


