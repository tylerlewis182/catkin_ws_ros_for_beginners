#!/usr/bin/env python

import rospy

if __name__=='__main__':

	# init node
	rospy.init_node('my_first_python_node')

	# print message to console 
	rospy.loginfo("This node has been started")

	# create a rate object with frequency 10 Hz
	rate = rospy.Rate(10)

	# run until this node is shutdown
	while not rospy.is_shutdown():

		rate.sleep() # try to keep the rate at 10 Hz
		rospy.loginfo("Hello")
