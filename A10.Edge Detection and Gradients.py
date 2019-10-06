import cv2 
import numpy as np

# 颜色过滤：只显示单帧中特定范围内的颜色
cap = cv2.VideoCapture(0)

while True:
  _,frame = cap.read()
  # 转换至HSV颜色空间，H表示色彩[0,179]，S表示饱和度[0,255]，V表示亮度[0,255]
  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
  
  k = cv2.waitKey(5) & 0xFF  # 显示完一帧图像后延迟5ms显示下一帧，waitKey函数返回值是按键值
  if k ==27:
    break
    
cv2.destroyAllWindows()
cap.release()
