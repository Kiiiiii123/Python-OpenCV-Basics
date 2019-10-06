# 图像梯度原理简单来说就是求导 OpenCV提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr和Laplacian。Sobel和Scharr是求一阶或二阶导数。Scharr是对Sobel（使用小的卷积核求解梯度角度时）的优化，Laplacian是求二阶导数。
import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  _,frame = cap.read()

  laplacian = cv2.Laplacian(frame.cv2.CV_64F)
  sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize = 5)
  sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize = 5)
  
  cv2.imshow('origin',frame)
  cv2.imshow('laplacian',laplacian)
  cv2.imshow('sobelx',sobelx)
  cv2.imshow('sobely',sobely)
  
  k = cv2.waitKey(5) & 0xFF  # 显示完一帧图像后延迟5ms显示下一帧，waitKey函数返回值是按键值
  if k ==27:
    break
    
cv2.destroyAllWindows()
cap.release()
