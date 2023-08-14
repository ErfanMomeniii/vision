import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # height of the frame

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # choose codec

# create VideoWriter object w by h, 30 frames per second
out = cv2.VideoWriter('eggs-reverse.avi', fourcc, 300.0, (w, h))
a = []
while True:
    ret, I = cap.read()

    if ret == False:  # end of video (or error)
        break

    # write the current frame I
    print(I.shape)
    a.append(I)
list.reverse(a)
for a2 in a:
    out.write(a2)
cap.release()
out.release()
