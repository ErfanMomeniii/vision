import face_recognition
import cv2

image = cv2.imread("i.jpeg")
face_locations = face_recognition.face_locations(image)
cv2.imshow("image",image)
cv2.waitKey(0)
print("found %d face(s)" % len(face_locations))

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.imshow("face", image[top:bottom, left:right])
    cv2.waitKey(0)
