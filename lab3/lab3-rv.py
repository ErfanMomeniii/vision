import numpy as np
import cv2

cap = cv2.VideoCapture('eggs.avi')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('eggs-reverse.avi', fourcc, 300.0, (w, h))
a = []
while True:
    ret, I = cap.read()

    if ret is False:
        break

    print(I.shape)
    a.append(I)
list.reverse(a)
for a2 in a:
    out.write(a2)
cap.release()
out.release()
