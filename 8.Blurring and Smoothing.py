# Color Filtering一节中仍然存在很多的背景噪声，最简单去噪声的方法是模糊平滑
import cv2 
import numpy as np

# 颜色过滤：只显示单帧中特定范围内的颜色
cap = cv2.VideoCapture(0)

while True:
  _,frame = cap.read()
  # 转换至HSV颜色空间，H表示色彩[0,179]，S表示饱和度[0,255]，V表示亮度[0,255]
  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
  # 设定蓝色的阈值
  lower_red = np.array([110,50,50])
  upper_red = np.array([130,255,255])
  
  # 根据阈值构建掩膜,该掩膜对frame特定
  mask = cv2.inRange(hsv,lower_red,upper_red)
  
  # 对原图和掩膜进行位运算
  res = cv2.bitwise_and(frame,frame,mask = mask) 
  
  # 均值滤波
  kernel = np.ones((15,15),np.float32)/225
  smoothed = cv2.filter2D(res,-1,kernel)
  
  # 高斯模糊
  blur = cv2.GaussianBlur(res,(15,15),0)
  
  # 中值模糊
  medianblur = cv2.medianBlur(res,15)
  
  # 显示图像
  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res)
  cv2.imshow('smoothed',smoothed)
  cv2.imshow('blur',blur)
  cv2.imshow('medianblur',medianblur)
  
  k = cv2.waitKey(5) & 0xFF  # 显示完一帧图像后延迟5ms显示下一帧，waitKey函数返回值是按键值
  if k ==27:
    break
    
cv2.destroyAllWindows()
cap.release()
