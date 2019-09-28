import cv2
import numpy as np

# 针对Web Camera输入或者是视频文件
cap=cv2.VideoCapture(0) 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
  # rec返回True或者False
  rec,frame=cap.read()
  
  # 转换灰色
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  out.write(frame)
  
  # 出现两个窗口
  cv2.imshow('frame',frame)
  cv2.imshow('gray',gray)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
    
cap.release()
out.release()
cv2.destroyAllWindows()
