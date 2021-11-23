import numpy as np
from cv2 import cv2

# Create variable that holds our image
img = cv2.imread('Camera_Assets/ChessBoard.jpeg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Corner Detection == (src image, number of corners, minimum quality, minimum euclidean distance)
corners = (cv2.goodFeaturesToTrack(gray, 100, 0.01, 10))
# Cast to integer since goodFeaturesToTrack returns floating points
corners = np.int0(corners)

# Draw a circle around each corner
for corner in corners:
    # ravel flattens arrays
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (0, 0, 255), 1)


cv2.imshow('Chess', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
