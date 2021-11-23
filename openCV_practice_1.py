from cv2 import cv2

# Open an image
img = cv2.imread('Camera_Assets/7V.jpeg', -1)

# Resize an image
img = cv2.resize(img, (400, 400))

# Show the image
cv2.imshow('Image', img)

# Wait x seconds for a key to be pressed then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
