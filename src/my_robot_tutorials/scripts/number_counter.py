#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

# global variables
counter = 0
pub = None


# functions
def callback_number(msg):
	global counter
	counter += msg.data
	new_msg = Int64()
	new_msg.data = counter
	pub.publish(new_msg)

	

# main
if __name__=='__main__':

	# init node 
	rospy.init_node('number_counter')

	# create a subscriber
	sub = rospy.Subscriber("/number", Int64, callback_number)

	# create a publisher
	pub = rospy.Publisher("/number_count", Int64, queue_size=10)

	# keep this node running
	rospy.spin()
