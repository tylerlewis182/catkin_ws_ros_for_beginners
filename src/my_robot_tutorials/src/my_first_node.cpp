#include <ros/ros.h>

int main(int argc, char* argv[])
{
	// init node (NOTE: can't have two nodes with the same name running at the same time)
	ros::init(argc, argv, "my_first_cpp_node");

	// create a rosnode handle
	ros::NodeHandle nh;

	// print message to console
	ROS_INFO("Node has been started");

	// // create duration object and sleep for 1 second
	//ros::Duration(1.0).sleep();

	// create a rate object at 10 Hz
	ros::Rate rate(10); // 10 Hz

	while(ros::ok())
	{
		ROS_INFO("Hello");
		rate.sleep(); // try to keep the loop at 10 Hz
	}

	return 0;
}
