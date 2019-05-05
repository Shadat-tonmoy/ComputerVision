import numpy as np
import cv2 as openCV

width = 720
height = 1024

input_image = openCV.imread("../images/me.jpg")

image_width, image_height = input_image.shape[:2]

if image_width > width:
    width = int(image_width / 10)

if image_height > height:
    height = int(image_height / 10)

input_image = openCV.resize(input_image, (height, width))

blurred_image = openCV.GaussianBlur(input_image, (9, 9), 0)

canny_edged = openCV.Canny(blurred_image, 10, 70)

# _, sketched =  openCV.threshold(canny_edged, 70, 255, openCV.THRESH_BINARY_INV)

_, sketched = openCV.pencilSketch(input_image, sigma_s=40, sigma_r=0.20, shade_factor=0.05)

sketched = openCV.cvtColor(sketched, openCV.COLOR_BGR2GRAY)

openCV.imshow("Original Image", sketched)

openCV.waitKey()



openCV.destroyAllWindows()


