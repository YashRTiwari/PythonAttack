import cv2, time

# 0 - camera
# "file name" - video
video = cv2.VideoCapture(0)

no_of_frame = 1;


# boolean, numpyarray
while True:
    no_of_frame = no_of_frame + 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(10)

    if key == ord('q'):
        print(no_of_frame)
        break

cv2.destroyAllWindows()


video.release()
