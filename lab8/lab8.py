import cv2
import numpy as np

I = cv2.imread('square.jpg')
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
G = np.float32(G)
window_size = 2
soble_kernel_size = 3
alpha = 0.04
H = cv2.cornerHarris(G, window_size, soble_kernel_size, alpha)
print(H)
H = H / H.max()
C = np.uint8(H > 0.005) * 255
nc,CC = cv2.connectedComponents(C)
nC, CC, stats, centroids = cv2.connectedComponentsWithStats(C)
J = I.copy()
for i in range(1, nC):
    cv2.circle(J, (int(centroids[i, 0]), int(centroids[i, 1])), 3, (0, 0, 255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(J, 'There are %d corners!' % (nC-1), (20, 80), font, 1, (0, 0, 255), 2)
cv2.imshow('corners', J)
cv2.waitKey(0)  # press any key
cv2.destroyAllWindows()
