#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class ThirdNode(Node): 
    def __init__(self):
        super().__init__("pipline_step_3") 
        self.count_=0
        self.sub_= self.create_subscription(Float64, "data_2", self.calback_fonction, 10)
        self.pub_= self.create_publisher(Float64,"data_3",10)
        self.tim_=self.create_timer(1, self.calback_fonction)
#       self.get_logger().info("Smartphone has been started.")    
            
    def calback_fonction(self, msg):
        self.count_ += msg.data
        new_msg=Float64()
        new_msg.data= self.count_
        self.pub_.publish(new_msg)
        self.get_logger().info(str(msg.data))
        



def main(args=None):
    rclpy.init(args=args)
    node = ThirdNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
