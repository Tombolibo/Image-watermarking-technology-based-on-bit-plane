import numpy as np
import cv2

img = np.fromfile(r'./pics/key.png',dtype=np.uint8)
img = cv2.imdecode(img, -1)

cv2.imshow('img src', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = np.zeros((img.shape[0], img.shape[1], 8), dtype = np.uint8)
for i in range(8):
    x[:,:,i] = 2**i
bitPlane = np.zeros((img.shape[0], img.shape[1], 8), dtype = np.uint8)
for i in range(8):
    bitPlane[:,:,i] = cv2.bitwise_and(img, x[:,:,i])
    mask = bitPlane[:,:,i]>0
    bitPlane[:,:,i][mask] = 255
    cv2.imshow('bit plane{}'.format(i), bitPlane[:,:,i])
cv2.waitKey()