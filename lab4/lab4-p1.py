import numpy as np
import cv2

I = cv2.imread('isfahan.jpg', cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float64) / 255
sigma = 0.04
J = I.copy()
while True:
    cv2.imshow('isfahan', J)
    key = cv2.waitKey(33)
    if key & 0xFF == ord('u'):  # if 'u' is pressed
        sigma += 0.01
        if sigma > 1:
            sigma = 1
        J = I.copy() + sigma * np.random.randn(*I.shape)
        J[J > 1] = 1
        J[J < 0] = 0
        cv2.imshow('isfahan', J)
    elif key & 0xFF == ord('d'):  # if 'd' is pressed
        sigma -= 0.01
        if sigma < 0:
            sigma = 0
        J = I.copy() + sigma * np.random.randn(*I.shape)
        J[J > 1] = 1
        J[J < 0] = 0
        cv2.imshow('isfahan', J)
    elif key & 0xFF == ord('q'):  # if 'q' is pressed then
        break  # quit
cv2.destroyAllWindows()
