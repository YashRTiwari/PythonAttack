import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
# Scale factor - decrease 5%
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor= 1.1,
                                      minNeighbors= 5)

# Draw rectangle
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), 3)


print(faces)
print(type(faces))


resize_img = cv2.resize(img, (int(img.shape[1]/1.10), int(img.shape[0]/1.10)))

cv2.imshow("GRAY", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
