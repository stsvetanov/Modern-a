# https://github.com/shomnathsomu/crack-detection-opencv

# importing necessary libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read a cracked sample image
# img = cv2.imread('Input-Set/Cracked_07.jpg')
img = cv2.imread('P1040047.JPG')


blur = cv2.GaussianBlur(img, (25, 25), 0)
sub = cv2.subtract(blur,img)
sobelx = cv2.Sobel(sub, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(sub, cv2.CV_64F, 0, 1, ksize=3)
outim = np.sqrt(sobelx ** 2 + sobely ** 2)
cv2.imshow('Output', outim)
cv2.waitKey()