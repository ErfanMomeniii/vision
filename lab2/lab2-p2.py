import cv2
import numpy as np

d = cv2.imread('damavand.jpg')
e = cv2.imread('eram.jpg')
dp = 1
ep = 0
while dp > 0:
    k = cv2.addWeighted(d, dp, e, ep, 0)
    cv2.imshow('blending', k)
    cv2.waitKey(1)
    dp -= 0.001
    ep += 0.001

cv2.destroyAllWindows()
