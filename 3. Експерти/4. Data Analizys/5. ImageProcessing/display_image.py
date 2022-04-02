import cv2

# Load an color image in grayscale
# img = cv2.imread('images/multiple-blob.png', 0)

# Load an color image in color
img = cv2.imread('images/multiple-blob.png', cv2.IMREAD_COLOR)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
