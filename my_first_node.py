
#!/usr/bin/env python3

from itertools import count
import rclpy #importation de la bib python 
from rclpy.node import Node# the imporation of the node class from the ros bib based on python 
class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Digital Twin1")
        self.create_timer(0.5, self.timer_callback) #creation d'un timer pour appelz la fonction
        
    def timer_callback(self):
        self.counter_ +=1
        self.get_logger().info("Hello "+ str(self.counter_))
def main(args=None):# the creation of the main function
    rclpy.init(args=args) #initialise the ros2 communication
    node = MyNode() #creation of the ode  message that will be printed by the node 
    rclpy.spin(node) #make the node to be alive 
    rclpy.shutdown() # the kill ros2 communication



if __name__ == "__main__":
    main()