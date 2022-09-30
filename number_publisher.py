#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisher(Node):
    
    def __init__(self):
        super().__init__("number_publisher")
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(0.2, self.timer_callback)
        self.number = 0
        self.get_logger().info("Number Publisher has started!!")

    def timer_callback(self):
        msg = Int64()
        msg.data = self.number
        self.get_logger().info(str(msg.data+1))
        self.number += 1
        self.publisher.publish(msg)
        
def main(args=None):
        rclpy.init(args=args)
        node = NumberPublisher() 
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()