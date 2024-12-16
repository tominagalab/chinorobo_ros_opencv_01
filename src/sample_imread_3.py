#!/usr/bin/env python

import cv2
img1 = cv2.imread('/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img01.jpg')
img2 = cv2.imread('/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img02.jpg')
img3 = cv2.imread('/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img03.jpg')

cv2.imshow('input1', img1)
cv2.imshow('input2', img2)
cv2.imshow('input3', img3)

while True:
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
