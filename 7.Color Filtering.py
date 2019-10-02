import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  _,frame = cap.read()
  # 转换至HSV颜色空间，H表示色彩[0,179]，S表示饱和度[0,255]，V表示亮度[0,255]
  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
