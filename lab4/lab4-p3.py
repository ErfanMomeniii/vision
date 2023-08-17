import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255
m = 13
Fg = cv2.getGaussianKernel(m, sigma=-1)
print(Fg)
print(Fg.shape)
Fg = Fg.dot(Fg.T)
print(Fg)
print(Fg.shape)
Jg = cv2.filter2D(I, -1, Fg)
cv2.imshow('original', I)
cv2.waitKey()
cv2.imshow('blurred_Gaussian', Jg)
cv2.waitKey()
cv2.destroyAllWindows()
