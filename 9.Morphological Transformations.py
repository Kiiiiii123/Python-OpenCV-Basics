# 上一节介绍的平滑模糊去除噪声的方法是不够的，形态学转换是去除白噪声更好的方法
# 形态学转换一般情况下对二值化图像进行，基本操作为腐蚀和膨胀，他们的变体构成了开运算，闭运算，梯度等。
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
  
  # 腐蚀 把前景物体的边界腐蚀掉，但是前景仍然是白色的。卷积核沿着图像滑动，如果与卷积核对应的原图像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零。根据卷积核的大小靠近前景的所有像素都会被腐蚀掉（变为0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除白噪音很有用也可以用来断开两个连在一块的物体。
  kernel = np.omes((4,4),np.uint8)
  erosion = cv2.erode(mask,kernel,,iterations = 1)
  
  # 膨胀 与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元素的像素值就是1。所以这个操作会增加图像中白色区域（前景）。一般在去噪音时先腐蚀再膨胀，因为腐蚀再去掉白噪音的同时，也会使前景对象变小，所以我们再膨胀。这时噪音已经被去除，不会再回来了，但是前景还在并会增加，膨胀也可以用来连接两个分开的物体。
  dilation = cv2.dilate(mask,kernel,iterations = 1)
  
  # 开运算是先腐蚀后膨胀的过程，可以消除图像上细小的噪声，并平滑物体的边界
  opening = cv2.morphologyEX(mask,cv2.MORPH_OPEN,kernel)
  
  # 闭运算是先膨胀后腐蚀的过程，可以填充物体内细小的空洞，并平滑物体边界
  closing = cv2.morphologyEX(mask,cv2.MORPH_CLOSE,kernel)
  
  # 显示图像
  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res)
  cv2.imshow('erosion',erosion)
  cv2.imshow('dilation',dilation)
  cv2.imshow('opening',opening)
  cv2.imshow('closing',closing)
  
  k = cv2.waitKey(5) & 0xFF  # 显示完一帧图像后延迟5ms显示下一帧，waitKey函数返回值是按键值
  if k ==27:
    break
    
cv2.destroyAllWindows()
cap.release()
