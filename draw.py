import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain colour
# blank[200:300,100:400] = 0,0,255
# cv.imshow('Green',blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness = 2)
cv.imshow('Rectangle',blank)

cv.waitKey(0)