import numpy as np
import cv2 as openCV


'''
Perspective transformation  allows us to get an fit image from a skewed one. It requires
* Coordinate of the 4 corners of the original image
* Coordinate of the 4 corners of the desired output imagee
* Using this two sets of 4 points compute a Perspective  Transformation matrix
* Apply this matrix on the image using Warp Affine method
'''

input_image = openCV.imread("./images/scan.jpg")

openCV.imshow("Original Image", input_image)

openCV.waitKey()

# openCV.destroyAllWindows()

corner_points = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

output_points  = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

perspective_transformation_matrix = openCV.getPerspectiveTransform(corner_points, output_points)

warped_image = openCV.warpPerspective(input_image, perspective_transformation_matrix, (420, 594))

openCV.imshow("Transformed Image", warped_image)

openCV.waitKey()

openCV.destroyAllWindows()
