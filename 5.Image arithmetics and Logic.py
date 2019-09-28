import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('Main-SVM-Image.png')
img3 = cv2.imread('Main-Logo.png')

# 第一部分：图像的逻辑运算
add1 = img1 + img2
# 将全部的像素值相加在一起
add2 = cv2.add(img1,img2)
# 加权，0代表γ值
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

cv2.imshow('add1',add1)
cv2.imshow('add2',add2)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 第二部分：阈值
rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]
# 先对img3转灰度
img3gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
# 根据阈值220进行二分
ret,mask=cv2.threshold(img3,220,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('mask',mask)
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img3_fg=cv2.bitwise_and(img3,img3,mask=mask)

dst=cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols]=dst

cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img3_fg',img3_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
