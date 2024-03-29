# 可以简单理解为爬虫并初步处理图片的过程
import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
  neg_images_link = 'website like : http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
  neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
  
  if not os.path.exists('neg'):
    os.makedirs('neg')
    
  pic_num = 1
  for i in neg_image_urls.split('\n'):
    try:
      print(i)
      urllib.request.urlretrieve(i,'neg/'+str(pic_num)+'.jpg')
      img = cv2.imread('neg/'+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
      resized_img = cv2.resize(img,(100,100))
      cv2.imwrite('neg/'+str(pic_num)+'.jpg',resized_img)
      pic_num +=1
      
    except Exception as e:
      print(str(e))
      
store_raw_images()
