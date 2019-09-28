import cv2
import numpy as np

img = cv2.imread('MyImage.jpg',cv2.IMREAD_COLOR)

# 画直线，注意颜色是BGR
cv2.line(img,(0,0),(150,150),(255,0,0),15)

# 画长方形
cv2.rectangle(img,(15,25),(200,150),(255,255,255),5)

# 画圆形，-1表示填充
cv2.circle(img,(100,63),55,(0,0,255),-1)

imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
