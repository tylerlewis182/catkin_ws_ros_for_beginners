#include <ros/ros.h>
#include <std_msgs/String.h>


void receive_radio_data_cb(const std_msgs::String& msg)
{
	ROS_INFO("Message received: %s", msg.data.c_str());
}


// main
int main(int argc, char* argv[])
{
	ros::init(argc, argv, "smartphone");
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("/robot_news_radio", 1000, receive_radio_data_cb);
	ros::spin();
}

/*

Add the following 2 lines to 'my_robot_tutorials' CMakeLists.txt:

	add_executable(smartphone src/smartphone.cpp)
	target_link_libraries(smartphone ${catkin_LIBRARIES})

*/
