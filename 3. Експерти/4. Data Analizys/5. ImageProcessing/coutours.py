import cv2

# Load an color image in grayscale
# img = cv2.imread('images/multiple-blob.png', 0)

# Load an color image in color
img = cv2.imread('images/multiple-blob.png', cv2.IMREAD_COLOR)
# img = cv2.imread('images/plate.jpg', cv2.IMREAD_COLOR)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
ret, thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV)

cnts = cv2.findContours(thresh, cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)[0]

s_min = 1500
s_max = 10000
xcnts = []
coordinates = []

for cnt in cnts:
    if s_min < cv2.contourArea(cnt) < s_max:
        xcnts.append(cnt)
        M = cv2.moments(cnt)

        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 10, (0, 255, 0), -1)

        epsilon = 0.1 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True);
        cv2.drawContours(img, approx, -1, (0, 255, 0), 6)

        coordinates.append((cX, cY))

print(f"Dots number: {len(xcnts)}")
print(f"Coordinates: {coordinates}")

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
