#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddIntsClient(Node):
    
    def __init__(self):
        super().__init__("add_ints_client")
        self.call_add_server(4,5)
        
    def call_add_server(self, a, b):
        client = self.create_client(AddTwoInts, 'add_ints')
        while not client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server')
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_add_ints, a = a, b = b))
    
    def callback_add_ints(self, future, a, b):
        try:
            response =future.result()
            self.get_logger().info(str(a) + '+' + str(b) + '=' + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e,))

def main(args=None):
    rclpy.init(args=args)
    node = AddIntsClient()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()