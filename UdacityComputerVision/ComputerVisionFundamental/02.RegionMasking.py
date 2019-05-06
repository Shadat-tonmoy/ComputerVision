import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image = mpimg.imread("../images/test.jpg")

print("Image Type ", type(image), "Dimension ", image.shape)

y_size = image.shape[0]
x_size = image.shape[1]

region_select = np.copy(image)

'''
Defining the coordinates of region of interest which is a triangle. This triangle has three points left bottom
right bottom and apex. It has three line which follow the equation y = ax + b

We can find the value of a and b using numpy polyfit function by passing the x, y and degree of equation value as a 
parameter. Here the x and y indicates the point through which the line passes.
 
'''

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

print(fit_left)

'''
Meshgrid allows to build a coordinate matrix from two list of x's and y's. Details on Meshgrid can be found in the link
https://www.youtube.com/watch?v=KlTAmfqwD0E
It returns a list of X's and Y's which build the coordinate set 
'''
XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))

# print(XX)
# print(YY)

# print(fit_left[0])

region_threshold = (YY > (fit_left[0] * XX + fit_left[1])) & \
                   (YY > (fit_right[0] * XX + fit_right[1])) \
                   & (YY < (fit_bottom[0] * XX + fit_bottom[1]))

print(region_threshold)

region_select[region_threshold] = [255, 0, 0]

plt.imshow(region_select)

plt.show()