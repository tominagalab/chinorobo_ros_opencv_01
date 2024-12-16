#!/usr/bin/env python

import rospy
import cv2

IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img01.jpg'
img = cv2.imread(IMG_PATH)

rospy.init_node('sample_opencv_01')

cv2.imshow('input', img)

while not rospy.is_shutdown():
  cv2.waitKey(1)

cv2.destroyAllWindows()
