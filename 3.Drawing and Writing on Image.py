import cv2
import numpy as np

img = cv2.imread('MyImage.jpg',cv2.IMREAD_COLOR)

# 画直线，注意颜色是BGR
cv2.line(img,(0,0),(150,150),(255,0,0),15)

# 画长方形
cv2.rectangle(img,(15,25),(200,150),(255,255,255),5)

# 画圆形，-1表示填充
cv2.circle(img,(100,63),55,(0,0,255),-1)

# 画多段线
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts=pts.reshape((-1,1,2))
# True决定要不要将最后一个点与第一个点相连接形成闭环多边形
cv2.polylines(img,[pts],True,(0,255,255),3)

# 加文本，1表示字体大小，2表示字体粗细
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130),font,1,(200,250,250),2,cv2.LINE_AA)

imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
