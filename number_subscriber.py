#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):

        super().__init__("number_counter")
        self.counter_=0

        self.number_subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.pub_no=self.create_publisher(Int64,"number_count", 10)
        #self.first_timer_=self.create_timer(1, self.callback_number)
        self.server_=self.create_service(SetBool,"reset_counter",self.callback_reset_counter)
        #self.get_logger().info("hello iam a service node")

        self.get_logger().info("this is the number_counter_node!")

    def callback_number(self, msg):
        self.counter_ += msg.data
        new_msg=Int64()
        new_msg.data= self.counter_
        self.pub_no.publish(new_msg)

        self.get_logger().info(str(new_msg))
    def callback_reset_counter(self, request, response ):
        if request.data:
            self.counter_=0
            response.success= True
            response.message="reseted"
        else:
            response.success=False
            response.messages="not reseted"
        return response
        #self.activated_ = request.data
        #response.success = True
        #if self.activated_:
        #    response.message = "Robot has been activated"
       # else:
         #   response.message = "Robot has been deactivated"
        #return response
 #//////////////////////////////////////////////////////////////////
#response.sum= request.a * request.b
# self.get_logger().info(str(request.a) + "*" + str(request.b) + "=" + str(response.sum))



def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
