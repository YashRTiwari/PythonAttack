import cv2

# load, read, resize and save

# Reading an image with open cv
# 1 - color,
# 0 - grayscale,
# -1 - color image with alpha channel
img = cv2.imread("image.jpg", 0)

print(type(img))
print(img)
print(img.shape) #Image matrix size
print(img.ndim) #Image Band

# To resize

# resized_image = cv2.resize(img, (500, 500))
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))


# TO show an image
cv2.imshow("Image", resized_image)
# 0 - close on key press
# else - time in milli, cv2.waitKey(2000)
cv2.waitKey(0)
cv2.destroyAllWindows()