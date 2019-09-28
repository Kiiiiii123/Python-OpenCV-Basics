import cv2
import numpy as np

img = cv2.imread('MyImage.jpg',cv2.IMREAD_COLOR)

# 画直线，注意颜色是BGR
cv2.line(img,(0,0),(150,150),(255,0,0),15)

imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
