import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('Main-SVM-Image.png')
img3 = cv2.imread('Main-Logo.png')

# 逻辑运算
add1 = img1 + img2
# 将全部的像素值相加在一起
add2 = cv2.add(img1,img2)
# 加权，0代表γ值
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels = img3.shape
roi = img[0:rows,0:cols]

cv2.imshow('add',add)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
