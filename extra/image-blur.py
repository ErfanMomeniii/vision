import cv2
import numpy as np
from matplotlib import pyplot as plt

f, p = plt.subplots(2, 2)

image = cv2.imread('isfahan.jpg')
p[0, 0].imshow(image)
p[0, 0].title.set_text('original')
p[0, 0].axis('off')

Gaussian = cv2.GaussianBlur(image, (11, 11), 0)
p[0, 1].imshow(Gaussian)
p[0, 1].title.set_text('gaussian')
p[0, 1].axis('off')

median = cv2.medianBlur(image, 5)
p[1, 0].imshow(Gaussian)
p[1, 0].title.set_text('median')
p[1, 0].axis('off')

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
p[1, 1].imshow(bilateral)
p[1, 1].title.set_text('bilateral')
p[1, 1].axis('off')

plt.show()
