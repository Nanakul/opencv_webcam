from cv2 import cv2
import numpy as np

# Modified code from file 3, but this code just displays the capture device.
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    # Draw a line == (src image, starting pos, ending pos, color, line thickness)
    # Draw a BLUE line and then a GREEN line
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # Draw a RED rectangle around the image
    img = cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), 5)

    # Draw a RED circle == (src image, center pos, radius, color, line thickness)
    img = cv2.circle(img, (960, 540), 60, (0, 0, 255), 5)

    # Draw text on the image == (src img, Text, Bottom Left pos, font, scale, color, thickness, line type)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Midi is cool!', (50, height - 10), font, 3, (0, 0, 255), 5, cv2.LINE_AA)

    # Show the image
    cv2.imshow('Frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
