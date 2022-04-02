import cv2
im = cv2.imread('images/drone_station2.png') # read picture

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # BGR to grayscale

ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY)

countours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 0.2 * cv2.arcLength(countours[0], True)
approx = cv2.approxPolyDP(countours[1], epsilon, True)

cv2.drawContours(im, approx, -1, (0, 255, 0), 6)
cv2.imshow("Contour", im)

cv2.waitKey(0)
cv2.destroyAllWindows()