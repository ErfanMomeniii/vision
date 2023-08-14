import numpy as np
import cv2
i=cv2.imread('masoleh.jpg')
b=i[:,:,0]
g=i[:,:,1]
r=i[:,:,2]
cv2.imshow('Masoleh',i)

while 1:
    f = np.zeros(i.shape)
    k = cv2.waitKey()
    if k == ord('o'):
        cv2.imshow('Masoleh',i)
    elif k == ord('b'):
        f[:,:,0]=b
        cv2.imshow('b',f)
    elif k== ord('g'):
        f[:,:,1]=g
        cv2.imshow('g',f)
    elif k==ord('r'):
        f[:,:,2]=r
        cv2.imshow('r',f)
    elif k==ord('q'):
        cv2.destroyAllWindows()
        break
