import cv2

# path = "white dot.png"
# path = "images/drone_station2.png"
path = "images/white-dot.png"

# reading the image in grayscale mode

gray = cv2.imread(path, 0)
# threshold
th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                        cv2.CHAIN_APPROX_SIMPLE)[0]

# filter by area
s1 = 10
s2 = 20
xcnts = []
coordinates = []

for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)
        M = cv2.moments(cnt)

        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        coordinates.append((cX, cY))

print(f"Dots number: {len(xcnts)}")
print(f"Coordinates: {coordinates}")