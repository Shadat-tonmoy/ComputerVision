import numpy as np
import cv2

input = cv2.imread('./images/input.jpg')        # opening original image

B, G, R = input[150, 202]                       # extracting RGB value of a pixel into image grid

print input.shape                               # printing image shape. Image is represented as a 3D numpy array

print B, G, R                                   # printing the values of RGB

gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)        # converting original image to gray scale image

print gray_image.shape                  # printing gray scale image shape. Image is represented as a 3D numpy array

print gray_image[0, 125]                # printing gray scale value of a pixel

hsv_image = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

print hsv_image.shape

print ("HSV Hue Channel ", hsv_image[:, :, 0])
print ("HSV Saturation Channel ", hsv_image[:, :, 1])
print ("HSV Value Channel ", hsv_image[:, :, 2])

# cv2.imshow("HSV Image ",hsv_image)
# cv2.imshow("Hue Channel Image ", hsv_image[:, :, 0])
# cv2.imshow("Saturation Channel Image ", hsv_image[:, :, 1])
# cv2.imshow("Value Channel Image ", hsv_image[:, :, 2])

B, G, R = cv2.split(input)
cv2.imshow("Blue Channel Image ", B)
cv2.imshow("Red Channel Image ", R)
cv2.imshow("Green Channel Image ", G)

merged_image = cv2.merge([B, G, R])
cv2.imshow("Merged Image ", merged_image)

bluish_image = cv2.merge([B+100,G,R])
# cv2.imshow("Bluish Image ", bluish_image)


zeros = np.zeros(input.shape[:2], dtype="uint8")

blu_shaded = cv2.merge([B, zeros, zeros])

green_shaded = cv2.merge([zeros, G, zeros])

red_shaded = cv2.merge([zeros, zeros, R])


cv2.imshow("Blu Shaded", blu_shaded)
cv2.imshow("Red Shaded", red_shaded)
cv2.imshow("Green Shaded", green_shaded)


cv2.waitKey()

cv2.destroyAllWindows()



# cv2.imshow('Original Image',input)

# cv2.waitKey()

# cv2.destroyAllWindows()

