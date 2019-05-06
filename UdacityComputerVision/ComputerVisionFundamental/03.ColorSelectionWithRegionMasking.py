import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimage

image = mpimage.imread("../images/test.jpg")

y_size = image.shape[0]
x_size = image.shape[1]

color_select = np.copy(image)
line_select = np.copy(image)

red_threshold = 0
green_threshold = 0
blue_threshold = 0

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

color_threshold = (image[:, :, 0] < rgb_threshold[0]) | \
                  (image[:, :, 1] < rgb_threshold[1]) | \
                  (image[:, :, 2] < rgb_threshold[2])

# print(color_threshold)

XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))

region_threshold = (YY > (fit_left[0] * XX + fit_left[1])) & \
                   (YY > fit_right[0] * XX + fit_right[1]) & \
                   (YY < fit_bottom[0] * XX + fit_bottom[1])

print(region_threshold)

color_select[color_threshold] = [0, 0, 0]

line_select[~color_threshold & region_threshold] = [255, 0, 0]

plt.imshow(color_select)

plt.imshow(line_select)

plt.show()