import numpy as np
import cv2

cap = cv2.VideoCapture('eggs.avi')


while True:

    ret, I = cap.read()
    if ret is False:
        break

    cv2.imshow('eggs',I)
    
    key = cv2.waitKey(30)

    if key & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()


