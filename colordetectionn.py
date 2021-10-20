import cv2
import numpy as np
img1 = cv2.imread("C:\picture.png")
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
lower_blue= np.array([78,158,124])
upper_blue = np.array([138,255,255])
hsv=cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv, lower_red, upper_red)
cv2.imshow ("image",img1)
cv2.imshow ("Mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows() 