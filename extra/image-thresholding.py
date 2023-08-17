import cv2
import numpy as np
from matplotlib import pyplot as plt

f, p = plt.subplots(2, 4)

I = cv2.imread('isfahan.jpg', cv2.IMREAD_GRAYSCALE)  # or use 0
p[0, 0].imshow(I, 'gray')
p[0, 0].title.set_text('original')
p[0, 0].axis('off')

ret, thresh = cv2.threshold(I, 120, 255, cv2.THRESH_BINARY)
p[1, 0].imshow(thresh, 'gray')
p[1, 0].title.set_text('binary')
p[1, 0].axis('off')

ret, thresh = cv2.threshold(I, 120, 255, cv2.THRESH_TRUNC)
p[0, 1].imshow(thresh, 'gray')
p[0, 1].title.set_text('trunc')
p[0, 1].axis('off')

ret, thresh = cv2.threshold(I, 120, 255, cv2.THRESH_TOZERO)
p[1, 1].imshow(thresh, 'gray')
p[1, 1].title.set_text('toZero')
p[1, 1].axis('off')

thresh = cv2.adaptiveThreshold(I, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7,
                               5)  # block size always should be odd
p[0, 2].imshow(thresh, 'gray')
p[0, 2].title.set_text('mean')
p[0, 2].axis('off')

thresh = cv2.adaptiveThreshold(I, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7,
                               5)  # block size always should be odd
p[1, 2].imshow(thresh, 'gray')
p[1, 2].title.set_text('gaussian')
p[1, 2].axis('off')

ret, thresh = cv2.threshold(I, 120, 255, cv2.THRESH_BINARY +
                            cv2.THRESH_OTSU)
p[0, 3].imshow(thresh, 'gray')
p[0, 3].title.set_text('otsu')
p[0, 3].axis('off')

p[1, 3].axis('off')

plt.show()
