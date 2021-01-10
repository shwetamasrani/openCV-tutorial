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
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness = -1) #cv.FILLED
cv.imshow('Rectangle',blank)

# 3. Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness = 3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (420,250), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness = 2)
cv.imshow('Line',blank)

cv.waitKey(0)