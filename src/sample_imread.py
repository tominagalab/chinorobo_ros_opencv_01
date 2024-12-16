#!/usr/bin/env python

import cv2
img = cv2.imread('/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_01/resource/img01.jpg')
cv2.imshow('input', img)

while True:
	if cv2.waitKey(1) == 27:
		break


cv2.destroyAllWindows()
