#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__=='__main__':

	rospy.init_node('robot_news_radio_transmitter', anonymous=True) # anonymous
	# rospy.init_node('robot_news_radio_transmitter') # non-anonymous

	# create a publisher: (name of topic to publish to, type of message, queue size which acts like a buffe holds 10 messages)
	pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

	rate = rospy.Rate(2) # 2 Hz

	while not rospy.is_shutdown():
		msg = String()
		msg.data = "Hi, this is Dan from Robot News Radio!"
		pub.publish(msg)
		rate.sleep()

	rospy.loginfo("Node was stopped")
	