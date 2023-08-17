import numpy as np
import cv2

I = cv2.imread('isfahan.jpg')
I = I.astype(np.float) / 255
sigma = 0.4
N = np.random.randn(*I.shape) * sigma
J = I + N
cv2.imshow('original', I)
cv2.waitKey(0)

cv2.imshow('noisy image', J)
cv2.waitKey(0)
cv2.destroyAllWindows()
