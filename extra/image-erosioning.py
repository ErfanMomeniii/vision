import cv2
import numpy as np

I = cv2.imread('isfahan.jpg')
# Creating kernel
s = 5
# Using cv2.erode() method

cv2.imshow('isfahan', I)
while True:
    key = cv2.waitKey()

    if key & 0xFF == ord('u'):
        s += 1
        kernel = np.ones((s, s), np.uint8)
        image = cv2.erode(I, kernel)
        cv2.imshow('isfahan', image)
    if key & 0xFF == ord('d'):
        s -= 1
        if s < 1:
            s = 1
        kernel = np.ones((s, s), np.uint8)
        image = cv2.erode(I, kernel)
        cv2.imshow('isfahan', image)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
