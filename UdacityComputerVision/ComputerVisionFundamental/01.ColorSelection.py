import numpy as np
import matplotlib.image as mpimage
import matplotlib.pyplot as pyplot

image = mpimage.imread("../images/test.jpg")

print("The image is : ", type(image), "With Dimension ", image.shape)

y_size = image.shape[0]             # getting the height of image
x_size = image.shape[1]             # getting the width of image

color_select = np.copy(image)       # make a copy of the original image

red_threshold = 210                   # define the threshold for red channel
green_threshold = 210                 # define the threshold for red channel
blu_threshold = 210                   # define the threshold for red channel

rgb_threshold = [red_threshold, green_threshold, blu_threshold]


thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])

# print(thresholds)

color_select[thresholds] = [0,0,0]

pyplot.imshow(color_select)

pyplot.show()






