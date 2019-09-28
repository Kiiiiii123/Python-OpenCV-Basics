import cv2
import numpy as np

# 将暗光下的书本字体显现出来
img=cv2.imread('Bookpage.jpg')

# 直接加简单阈值，第三个参数就是当像素高于阈值时被赋予的新像素值，不同的阈值方法由第四个参数决定
retval,threshold1=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

# 先转换灰度后加阈值
grayScaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2=cv2.threshold(grayScaled,12,255,cv2.THRESH_BINARY)

# 加适应性阈值，文本显示效果最佳，根据图像上的每一个小区域计算对应的阈值，因此不同区域采用不同阈值，从而在亮度不同的情况下得到更好的效果
# cv2.ADAPTIVE_THRESH_MEAN_C 阀值取自相邻区域的平均值
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C 阀值取自相邻区域的加权和，权重为一个高斯窗口
# 11为计算阈值的区域大小
# 阀值等于平均值或者加权平均值减去常数2
gaus=cv2.adaptiveThreshold(grayScaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# Otsu's二值化
# retval与上面一样，是返回的阈值，Otsu's可以找到一个认为最好的阈值
retval,otsu=cv2.threshold(grayScaled,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold1',threshold1)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cvs.destroyAllWindows()
