import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_file = "image.png"
img = cv.imread(image_file, cv.IMREAD_UNCHANGED)

# Input image characteristics

print("Image dimension  :")
print("Image height     :")
print("Image width      :")
print("Number of channels: ")



plt.imshow(img)

cv.imshow("imazhi", img )
cv.waitKey(0)
cv.destroyAllWindows()
