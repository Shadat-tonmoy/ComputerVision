import os
import numpy as np
import cv2

path = "./images/bg"
compressed_path = "./images/bg_compressed/"

file_paths = []
file_names = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        file_paths.append(os.path.join(r, file))
        file_names.append(file)

for file_path, file_name in zip(file_paths,file_names):
    original_image = cv2.imread(file_path)
    height, width= original_image.shape[:2]
    print("Width ",width, "Height ",height)
    resized_image = cv2.resize(original_image, (int(width/5), int(height/5)),interpolation=cv2.INTER_AREA)
    cv2.imwrite(compressed_path+file_name,resized_image)
    print("Saved Successfully....")




