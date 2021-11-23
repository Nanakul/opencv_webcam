from cv2 import cv2
import numpy as np

# Store image in variable
img = cv2.imread('Camera_Assets/soccer_practice.jpeg', 0)
ball_img = cv2.imread('../Camera_Assets/ball.jpeg', 0)
h, w = ball_img.shape

# Six different methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# for loop to loop through the various methods to see which one
# gives the most accurate template
for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, ball_img, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # Performs a convolution; essentially involves taking the template
    # and sliding it around the base image to see how close of a match
    # there is in every single region of the base image.
    # (W - w + 1, H - h + 1) where 'W' == width of base image and 'w' == base of template image

    # last two methods, best to use min_location, that's why we use if statement here.
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # Set the bottom right corner of the rectangle
    bottom_right = (location[0] + w, location[1] + h)
    # Draw the rectangle around object
    cv2.rectangle(img2, location, bottom_right, 255, 5)

# Load the image
    cv2.imshow('Soccer Practice', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
