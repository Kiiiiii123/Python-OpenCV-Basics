# 通过读取下载的xml文件实现，这些文件每一个均代表了一类物体的特征表示，属于传统手动设计特征，可以进行自定义。
import cv2 
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.3,5)
  
  # 绘制矩形标注框
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # 眼睛不可能在脸部之外的区域被识别
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
      
   cv2.imshow('img',img)
   k = cv2.waitKey(30) & 0xFF
   if k == 27:
    break

cap.release()
cv2.destroyAllWindows()
    
