# Python code to find the co-ordinates of
# the contours detected in an image.
import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('i.jpeg', cv2.IMREAD_COLOR)
img2 = cv2.resize(img2, (640, 480), interpolation=cv2.INTER_LINEAR)

img2 = cv2.fastNlMeansDenoisingColored(img2, None, 10, 10, 7, 21)
img = cv2.Canny(img2, 100, 200)

_, threshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)
cv2.imshow('i', threshold)
cv2.waitKey()
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_TC89_KCOS)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.001 * cv2.arcLength(cnt, True), True)

    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)

    n = approx.ravel()

cv2.imshow('image2', img2)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
