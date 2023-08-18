import numpy as np
import cv2

I1 = cv2.imread('scene1.jpg')
I2 = cv2.imread('scene2.jpg')
cv2.imshow('Image 1 (background)', I1)
cv2.waitKey(0)
cv2.imshow('Image 2', I2)
cv2.waitKey(0)
K = np.abs(np.int16(I2) - np.int16(I1))
K = K.max(axis=2)
K = np.uint8(K)
cv2.imshow('The difference image', K)
cv2.waitKey(0)
threshold = 50
_, T = cv2.threshold(K, threshold, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((9, 9), np.uint8)
T = cv2.erode(T, kernel)
_, T = cv2.threshold(T, threshold, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresholded', T)
cv2.waitKey(0)
n, C = cv2.connectedComponents(T)
J = I2.copy()
J[T != 0] = [255, 255, 255]
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(J, 'There are %d toys!' % (n - 1), (20, 40), font, 1, (0, 0, 255), 2)
cv2.imshow('Number', J)
cv2.waitKey()
