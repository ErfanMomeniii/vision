import numpy as np
import cv2
import keyboard

cam_id = 0
cap = cv2.VideoCapture(cam_id)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('egg.avi', fourcc, 300.0, (640, 860))
l = []
lo = []
while True:
    ret, I = cap.read()
    out.write(I)
    lo.append(I)
    I = cv2.fastNlMeansDenoisingColored(I, None, 10, 10, 7, 10)
    l.append(I)
    if keyboard.is_pressed('q'):
        break

out.release()
cap.release()
for i in lo:
    cv2.imshow('original', i)
    cv2.waitKey(1)
cv2.destroyAllWindows()
for i in l:
    cv2.imshow('reduce noise', i)
    cv2.waitKey(1)
cv2.destroyAllWindows()
