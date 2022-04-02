from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im);
    # cv2.waitKey(0);

# capture frames from a camera with device index=0
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Can`t open the video file!\n");
    exit()

count = 1
count_decoded = 0
# loop runs if capturing has been initialized
while cap.isOpened():

    # reads frame from a camera
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    decodedObjects = decode(frame)
    display(frame, decodedObjects)
    # Display the frame
    # cv2.imshow('Camera', frame)
    if count > 10 and len(decodedObjects) > 0:
        count_decoded += 1

    print(f"Count: {count}, decoded: {count_decoded}, ratio: {count_decoded/count*100}")

    count += 1

    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera from video capture
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()



