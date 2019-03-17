#!/usr/bin/env python
import rospy
from rospy_tutorials.srv import AddTwoInts


# main
if __name__=='__main__':

	# create a node
	rospy.init_node('add_two_ints_client')

	# block until '/add_two_ints' service is advertised
	rospy.wait_for_service("/add_two_ints")

	# create client and call the service
	# NOTE: if the client fails to call the service, it will throw an exception
	try:
		# create the client
		add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)

		# call the client
		response = add_two_ints(2,6)
		rospy.loginfo("Sum is: " + str(response.sum))

	except rospy.ServiceException as e:
		rospy.logwarn("Service failed: " + str(e))

