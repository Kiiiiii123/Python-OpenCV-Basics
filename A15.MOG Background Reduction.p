# 从前一帧图像找出变化作为前景，不变的作为背景
import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4') 
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
  ret,frame = cap.read()
  fgmask = fgbg.apply(frame)
  
  cv2.imshow('origin',frame)
  cv2.imshow('fg',fgmask)
  
  k = cv2.waitKey(30) & 0xFF
  if k == 27:
    break
    
cap.release()
cv2.destroyAllWindows()
