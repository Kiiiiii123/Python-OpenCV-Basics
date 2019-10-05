# 上一节介绍的平滑模糊去除噪声的方法是不够的，形态学转换是去除白噪声更好的方法
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
  
  # fushi
  kernel = np.omes((4,4),np.uint8)
  erosion = cv2.erode(mask,kernel,,iterations = 1)
  
  # pengzhang
  dilation = cv2.dilate(mask,kernel,iterations = 1)
  
  # 显示图像
  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res)
  cv2.imshow('erosion',erosion)
  cv2.imshow('dilation',dilation)
  
  k = cv2.waitKey(5) & 0xFF  # 显示完一帧图像后延迟5ms显示下一帧，waitKey函数返回值是按键值
  if k ==27:
    break
    
cv2.destroyAllWindows()
cap.release()
