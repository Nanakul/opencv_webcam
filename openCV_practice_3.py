from cv2 import cv2
import numpy as np

# Load capture device
capture = cv2.VideoCapture(0)

# Use VideoCapture device
while True:
    # ret tells you if capture worked properly, frame is the image itself (numpy array)
    ret, frame = capture.read()

    # Get Height and Width of capture and cast to int so we can slice.
    # capture.get usually returns floating points.. that's why we cast
    width = int(capture.get(3))
    height = int(capture.get(4))

    # Create empty numpy array. Black canvas that is the size of our frame (webcam)
    # np.uint8 means 8-bit unsigned integer (0 to 255)
    image = np.zeros(frame.shape, np.uint8)

    # Shrink frame (webcam) image, and paste it four times.
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top Left
    image[height // 2:, :width // 2] = smaller_frame  # Bottom Left
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top Right
    image[height // 2:, width // 2:] = smaller_frame  # Bottom Right

    # Display the frame
    cv2.imshow('Frame', image)
    
    # if statement that essentially says, if 'q' is pressed, break.
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
