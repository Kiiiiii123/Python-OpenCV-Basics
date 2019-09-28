import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读入图像
#                                0
img=cv2.imread('MyImage.jpg',cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGER = -1

# 显示图像1
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 显示图像2,cv2读入图像数据为BGR，而matplotlib要显示则需要RGB
plt.imshow(img,cmap='gray',interpolation='bicubic')
# 在图像上画线
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

# 保存图像
cv2.imwrite('SaveImage.png',img)
