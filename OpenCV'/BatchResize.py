import glob
import cv2


def resize(f):
    image = cv2.imread(f,1)
    return cv2.resize(image, (100, 100))


for f in glob.glob("sample-images/*"):
    print("Starting "+f)
    resize_images = resize(f)
    cv2.imwrite(f, resize_images)
    print("Completed "+f)




