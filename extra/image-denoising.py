import cv2
import numpy as np

I = cv2.imread('isfahan.jpg')

I = cv2.fastNlMeansDenoisingColored(I, None, 10, 10, 7, 21)
cv2.imshow('isfahan', I)
cv2.waitKey()
cv2.destroyAllWindows()
