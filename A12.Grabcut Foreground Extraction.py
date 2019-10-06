# 图像前景分割
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-foreground-extraction.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
