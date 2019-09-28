import cv2
import numpy as np

img = cv2.imread('MyImage.jpg',cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
print(px)

# ROI:Region of Image
roi=img[100:155,100:155]
print(roi)

img[100:155,100:155]=[255,255,255]
# 图像区域复制转移
face=img[37:111,107:194]
img[0:74,0:87]=face

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
