#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

if __name__=='__main__':

	# init node 
	rospy.init_node('number_publisher')

	# create publisher
	pub = rospy.Publisher('/number', Int64, queue_size=10)

	# create a parameter - publish frequency
	publish_frequency = rospy.get_param("/number_publish_frequency")
	
	# create a parameter - example string parameter
	rospy.set_param("/another_param", "Hello")

	# create a rate object0 
	rate = rospy.Rate(publish_frequency) # Hz

	# publish until this node is shutdown
	while not rospy.is_shutdown():
		msg = Int64()
		msg.data = 2
		pub.publish(msg)
		rate.sleep()

	# send shutdown notification
	rospy.loginfo("'number_publisher' was stopped.")
