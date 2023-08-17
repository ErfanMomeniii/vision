import cv2
import numpy as np

I = cv2.imread('isfahan.jpg')
width = 640
height = 640
J = cv2.resize(I, (width, height))
while True:
    cv2.imshow('isfahan', J)
    key = cv2.waitKey()

    if key & 0xFF == ord('u'):
        width += 1
        height += 1
        J = cv2.resize(I, (width, height), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('isfahan', J)
    if key & 0xFF == ord('d'):
        width -= 1
        height -= 1
        J = cv2.resize(I, (width, height), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('isfahan', J)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
