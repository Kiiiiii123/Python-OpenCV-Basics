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
