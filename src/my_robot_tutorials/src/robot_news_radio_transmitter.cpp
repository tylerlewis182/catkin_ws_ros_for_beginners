#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char* argv[])
{
	// init node
	ros::init(argc, argv, "robot_news_radio_transmitter", ros::init_options::AnonymousName); // anonymous
	//ros::init(argc, argv, "robot_news_radio_transmitter"); // non-anonymous
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);

	ros::Rate rate(3); // Hz

	while(ros::ok())
	{
		std_msgs::String msg;
		msg.data = "Hi, this is William from the robot news radio";
		pub.publish(msg);
		rate.sleep();
	}
}

/*

Add these 2 lines to 'my_robot_tutorials' CMakeLists.txt:

	add_executable(robot_news_radio_transmitter src/robot_news_radio_transmitter.cpp)
	target_link_libraries(node_cpp ${catkin_LIBRARIES})

*/
