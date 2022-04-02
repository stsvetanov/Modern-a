import cv2

# Load an color image in grayscale
# img = cv2.imread('images/multiple-blob.png', 0)

# Load an color image in color
# img = cv2.imread('images/multiple-blob.png', cv2.IMREAD_COLOR)
img = cv2.imread('images/plate.jpg', cv2.IMREAD_COLOR)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
ret, thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)

cv2.imshow('image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
