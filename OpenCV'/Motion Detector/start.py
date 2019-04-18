import cv2, time
from  datetime import datetime
import pandas

video = cv2.VideoCapture(0)

first_frame = None
status_list = [None, None]
times = []
data_frame = pandas.DataFrame(columns=["Start Time", "End Time"])

while True:
    check, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Making it blur, to remove noise
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # Difference of two images
    delta_frame = cv2.absdiff(first_frame, gray)

    # applying threshold, returns tuble
    thres_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thres_delta = cv2.dilate(thres_delta, None, iterations= 2)

    (cnts,_) = cv2.findContours(thres_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (0, 255, 0), 3 )

    status_list.append(status_list)

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Blur Gray ", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold Frame", thres_delta)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(10)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
    print(status)

for i in range(0, len(times), 2):
    data_frame.append({"Start Time" : time[i], "End Time": time[i+1]}, ignore_index= True)

data_frame.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()


# 1. Should start with a static image
# 2. Object enter
# 3. Take difference
# 4. apply threshold

























