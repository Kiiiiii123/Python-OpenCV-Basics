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
      
# 存在链接中的图片不存在的情况  ，这里需要摆脱这些图片，新建一个uglies文件夹，复制其中一张图片到该文件夹中    
def find_uglies():
  for file_type in ['neg']:  # 可以是'pos'
    # 在neg文件夹下对图片进行遍历
    for img in os.listdir(file_type):
      # neg、pos文件夹下均存在ugly图片
      for ugly in os.listdir('uglies'):
        try:
          current_image_path = str(file_type)+'/'+str(img)
          ugly = cv2.imread('uglies/'+str(ugly))
          question = cv2.imread(current_image_path)
          
          if ugly.shape == question.shape and not (np.bitwise_xor(ugly,question).any()):
            print('Ugly!')
            os.remove(current_image_path)
            
        escept EXception as e:
          print(str(e))

# 创建描述文件          
def create_pos_n_neg():
  for file_type in ['neg']:
    for img in os.listdir(file_type):
      if file_type == 'neg':
        line = file_type+'/'+img+'\n'
        with open('bg.txt','a') as f:
          f.write(line)
      
      elif file_type == 'pos':
        line = file_type+'/'+img+'1 0 0 50 50\n'
        with open('bg.txt','a') as f:
          f.write(line)
          
create_pos_n_neg()          
# find_uglies()
# store_raw_images()
