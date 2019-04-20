import numpy as np
import cv2

input_image = cv2.imread("./images/input.jpg")

cv2.imshow("Original Image", input_image)

cv2.waitKey()

cv2.destroyAllWindows()

width, height = input_image.shape[:2]

startX, endX = int(width*0.25), int(width*0.75)

startY, endY = int(height*0.25), int(height*0.75)

cropped_image = input_image[startX:endX, startY:endY]

cv2.imshow("Cropped Image", cropped_image)

cv2.waitKey()

cv2.destroyAllWindows()



