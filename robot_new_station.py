#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewstation(Node): 

    def __init__(self):

        super().__init__("RobotNewstation") 
        self.declare_parameter("robot_name", "Robocon")
        self.dec_=self.get_parameter("robot_name").value
        self.declare_parameter("Publication_Freq", 1)
        self.freq_=self.get_parameter("Publication_Freq").value
    #create a publisher to a topic with a specifique msg type
        self.publishers_=self.create_publisher(String, "Robot_news", 10)
    # a timer that will call the self.publish_news function at 5HZ
        self.timer_= self.create_timer(1, self.publish_news)

    #print a message or a logger for the begin 
        self.get_logger().info("robot news station has been started")
        

    def publish_news(self):

        msg=String()
        msg.data =("Hi, this " + str(self.dec_) + " from the Robot News Station!")

        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewstation() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
