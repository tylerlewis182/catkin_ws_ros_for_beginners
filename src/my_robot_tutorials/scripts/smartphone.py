#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_receive_radio_data(msg):
	rospy.loginfo("Message received: ")
	rospy.loginfo(msg)



if __name__=='__main__':

	# init node
	rospy.init_node('smartphone')

	# create a subscriber: (name of topic to subscribe to, type of message, callback function)
	sub = rospy.Subscriber("/robot_news_radio", String, callback_receive_radio_data)

	# keep the script here with callback functionality until the 'robot_news_radio_receiver' node is stopped
	rospy.spin()
