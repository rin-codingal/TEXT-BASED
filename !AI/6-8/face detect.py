import cv2
#import cv2_imshow

# cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("!AI/6-8/haarcascade_frontalface_default.xml")

img = cv2.imread("!AI/6-8/person.jpg")
cv2.imshow("person", img)

# Cascade classifier takes only grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

#getting face location
face = face_cascade.detectMultiScale(gray_img, 1.3, 5)
print(face) # prints coordinates where the face exist

#draw rectangle on detected face
for(x, y, w, h) in face:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)  # green color rectangle with thickness of 3

cv2.imshow("face detection", img)

cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window