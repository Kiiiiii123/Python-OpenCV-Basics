# How to make your own Haar Cascade for Image and Video Object Detection?
# Steps:
# 1、Collect 'Negative' or 'Background' images.
# -Any image will do,just make sure your object is not present in them!Get thounds.
# 2、Collect or create 'Positive' images.
# -Thounds of images of your object.Can make these based on one image,or manually create them.
# 3、Create a positive vector file by stitching together all positives.
# -This is done with an OpenCV command.
# 4、Train cascade.
# -Done with OpenCV command.

# Negative abd Positive images need destription files:
# Negative images:
# Generally a bg.txt file that contains the path to each image,by line.
# Example line:neg/1.jpg
# Positive images:
# Sometimescalled 'info',pos.text,or something of this sort.Contains path to each image,by line,along with how many objects,and where they are located.
# Example line:pos/1.jpg 1 0 0 50 50 

# Notes:
# You want negative images larger than positive images generally,if you are going to 'create samples' rather than collect and label positives.
# Try to use small images.100*100 for negatives,50*50 for positives.
# Will get even smaller when it comes to training!
# Have ~ double positive images compared to negatives for training.
