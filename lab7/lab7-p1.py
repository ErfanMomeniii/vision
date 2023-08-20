import numpy as np
import cv2

I = cv2.imread('samand.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
G = cv2.GaussianBlur(G, (3, 3), 0)
canny_high_threshold = 200
min_votes = 100
min_centre_distance = 40
resolution = 1
circles = cv2.HoughCircles(G, cv2.HOUGH_GRADIENT,
                           resolution, min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes, minRadius=0, maxRadius=100)

for c in circles[0, :]:
    x = c[0]
    y = c[1]
    r = c[2]
    cv2.circle(I, (x.astype(np.uint8), y.astype(np.uint8)), r.astype(np.uint8), (0, 255, 0), 2)
    cv2.circle(I, (x.astype(np.uint8), y.astype(np.uint8)), 2, (0, 0, 255), 2)
cv2.imshow("I", I)
cv2.waitKey(0)
cv2.destroyAllWindows()
