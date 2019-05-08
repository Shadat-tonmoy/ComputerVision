import numpy as np
import matplotlib.pyplot as plt
import  matplotlib.image as mpimage
import cv2 as openCV


'''
Hough transformation is just transforming the xy image plane into p,theta hough space. It can be done easily by using 
openCV function. The function is called by :

lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap) Here,


we are operating on the image masked_edges (the output from Canny) and the output from HoughLinesP will be lines, which 
will simply be an array containing the endpoints (x1, y1, x2, y2) of all line segments detected by the transform 
operation. The other parameters define just what kind of line segments we're looking for.

*** masked_edges = detected edge image output from canny algorithm
*** rho, theta = (r,theta) is the distance and angular resolution of our grid in hough space  
*** In Hough space, we have a grid laid out along the (Θ, ρ) axis. We need to specify rho in units of pixels and theta
    in units of radians.
*** rho takes a minimum value of 1 and a reasonable starting place for theta is 1 degree (pi/180 in radian) 
*** The threshold parameter specifies the minimum number of intersections in a given grid cell a candidate line needs to 
    have to make it into the output. 
*** The empty np.array([]) is just a placeholder, no need to change it. 
*** min_line_length is the minimum length of a line (in pixels) that we will accept in the output.
*** max_line_gap is the maximum distance (again, in pixels) between segments that we will allow to be connected into a 
    single line.

'''

image = mpimage.imread("../images/exit-ramp.jpg")

gray_image = openCV.cvtColor(image, openCV.COLOR_RGB2GRAY)

kernel_size = 5

blurred_image = openCV.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)

low_threshold = 50
high_threshold = 150

edge = openCV.Canny(blurred_image, low_threshold, high_threshold)

rho = 1
theta = np.pi/180
threshold = 280
min_line_length = 310
max_line_gap = 30

line_image = np.copy(image) * 0

lines = openCV.HoughLinesP(edge, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

for line in lines:
    for x1, y1, x2, y2 in line:
        openCV.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

color_edges = np.dstack((edge, edge, edge))

line_over_image = openCV.addWeighted(color_edges, 0.8, line_image, 1, 0)

plt.imshow(line_over_image)

plt.show()



