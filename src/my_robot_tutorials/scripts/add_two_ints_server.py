#!/usr/bin/env python
import rospy
from rospy_tutorials.srv import AddTwoInts


# functions
def handle_add_two_ints(req):
	result = req.a + req.b
	rospy.loginfo("Sum of " + str(req.a) + " and " + str(req.b) + " is " + str(result))
	return result


# main
if __name__=='__main__':

	# init  node
	rospy.init_node("add_two_ints_server" )
	rospy.loginfo("Add two ints server node created")

	# create a service (service_name, message_type, callback_function)
	service = rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)
	rospy.loginfo("Service server has been started")

	# keep the service running until the 'add_two_ints_server' is shutdown
	rospy.spin()
	

'''
NOTES: AddTwoInts message type info can be found at:
       http://docs.ros.org/jade/api/rospy_tutorials/html/srv/AddTwoInts.html
       
       The service definition can be found in the file system of this computer;
       the file is located at:
       /opt/ros/kinetic/share/rospy_tutorials/srv/AddTwoInts.srv
'''
