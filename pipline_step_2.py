#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64


class SecondNode(Node): 
    def __init__(self):
        super().__init__("pipline_step_2") 
        self.counter_=0
        self.sub_no=self.create_subscription(Float64, "data_1", self.callback_fonction, 10)
        self.pub_no=self.create_publisher(Float64,"data_2", 10)

    def callback_fonction(self, msg):

        self.counter_ += msg.data
        new_msg=Float64()
        new_msg.data= self.counter_
        self.pub_no.publish(new_msg)
        self.get_logger().info(str(round(msg.data)))




def main(args=None):
    rclpy.init(args=args)
    node = SecondNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
