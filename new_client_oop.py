#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from functools import partial
from example_interfaces.srv import AddTwoInts

class ClientNode(Node): 
    def __init__(self):
        super().__init__("Client_1") #node name in the rqt_graph
        self.Call_service(5,7)
    def Call_service(self, a, b): #the request call function from server
        client=self.create_client(AddTwoInts, "add_two_service")

        while not client.wait_for_service(0.5):
            self.get_logger().warn("waiting for the server")
        request=AddTwoInts.Request()
        request.a=a
        request.b=b

        future=client.call_async(request) #we will call the server asynchronosly by giving the request
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))# a callback of the future

    def callback_call_add_two_ints(self, future, a, b):# the response call function from server

        try:
            response= future.result()
            self.get_logger().info(str(a)+ "   +   "+ str(b)+"   =   "+str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r"%(e,))
def main(args=None):
    rclpy.init(args=args)
    node = ClientNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
