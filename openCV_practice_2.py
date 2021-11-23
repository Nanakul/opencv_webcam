import random
from cv2 import cv2

# Create image variable
img = cv2.imread('../Camera_Assets/7V.jpeg', -1)

# for loop to manipulate pixels in the image
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copying part of the image, and pasting it elsewhere within the same image
# keyboard = img[500:600, 650:750]
# img[300:400, 550:650] = keyboard

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
