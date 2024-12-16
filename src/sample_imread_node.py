#!/usr/bin/env python

import rospy
import cv2

rospy.init_node('sample_imread_node')

img = cv2.imread('/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img01.jpg')

rate = rospy.Rate(1)
while not rospy.is_shutdown():
  rate.sleep()