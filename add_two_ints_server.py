#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddIntsServer(Node):
    
    def __init__(self):
        super().__init__("add_ints_server")
        self.server = self.create_service(AddTwoInts, 'add_ints', self.callback_add_ints)
        self.get_logger().info("Server Started")  
              
    def callback_add_ints(self, request, response):
        response.sum = request.a + request.b 
        self.get_logger().info(str(request.a) + '+' + str(request.b) + '=' + str(response.sum))
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = AddIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()