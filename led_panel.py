#!/usr/bin/env python3

from tkinter import S
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedStateArray
class LedPanalNode(Node):
    qos = QoSProfile(depth=10)

    def __init__(self):
        super().__init__("led_panel") 
        self.declare_parameter("led_state", [0, 0, 0])
        self.led_stat_=self.get_parameter("led_state").value
        self.server_=self.create_service(SetLed,"set_led",self.callback_add_tow_ints)
    
        self.get_logger().info("hello iam a service  server node")
        self.publi=self.create_publisher(LedStateArray, "led_state", self.qos)
        self.timer_=self.create_timer(1.0, self.publish_state)
        
    def callback_add_tow_ints(self, request, response):
        led_number=request.led_number
        state=request.state


        if led_number > len(self.led_stat_) or  led_number <= 0 :
            response.success = False
            return response
        if state not in [0,1]:
            response.success = False
            return response
        self.led_stat_[led_number - 1] = state
        response.success = True
        return response
    def publish_state(self):
        msg=LedStateArray()    
        msg.led_states= self.led_stat_
       # self.get_logger.info(msg)
        self.publi.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = LedPanalNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
