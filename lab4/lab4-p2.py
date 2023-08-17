import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255
m = 1
F = np.ones((m, m), np.float64) / (m * m)
J = cv2.filter2D(I, -1, F)

cv2.imshow('isfahan', J)

while True:
    key = cv2.waitKey()
    if key & 0xFF == ord('u'):
        m += 1
        F = np.ones((m, m), np.float64) / (m * m)
        J = cv2.filter2D(I, -1, F)
        cv2.imshow('isfahan', J)
    elif key & 0xFF == ord('d'):  # if 'd' is pressed
        m -= 1
        if m < 1:
            m = 1
        F = np.ones((m, m), np.float64) / (m * m)
        J = cv2.filter2D(I, -1, F)
        cv2.imshow('isfahan', J)
    elif key & 0xFF == ord('e'):  # if 'e' is pressed
        F = np.array([
            [-1, -1, -1], [-1, 8, -1], [-1, -1, -1]
        ])
        J = cv2.filter2D(I, -1, F)
        cv2.imshow('isfahan', J)
    elif key & 0xFF == ord('s'):  # if 's' is pressed
        F = np.array([
            [0, -1, 0], [-1, 5, -1], [0, -1, 0]
        ])
        J = cv2.filter2D(I, -1, F)
        cv2.imshow('isfahan', J)

    elif key & 0xFF == ord('b'):  # if 'b' is pressed
        F = np.ones((3, 3), np.float64) / 9
        J = cv2.filter2D(I, -1, F)
        cv2.imshow('isfahan', J)

    elif key & 0xFF == ord('g'):  # if 'g' is pressed
        F = np.array([
            [1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]
        ], np.float64)
        J = cv2.filter2D(I, -1, F / 256)
        cv2.imshow('isfahan', J)

    elif key & 0xFF == ord('q'):  # if 'q' is pressed then
        break  # quit
cv2.destroyAllWindows()
