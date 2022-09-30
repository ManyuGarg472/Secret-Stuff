#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
  
  
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.target_x = 15.0
        self.target_y = 6.0
        self.pose = None
        self.pub_vel = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.sub_pose = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.timer = self.create_timer(0.01, self.control_loop)
    
    def callback_turtle_pose(self,msg):
        self.pose = msg
        
      
    def control_loop(self):
        if self.pose == None:
            return
        dist_x = self.target_x - self.pose.x
        dist_y = self.target_y - self.pose.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        msg = Twist()
        if distance > 0.5:
            msg.linear.x = distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose.theta
            
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                
            msg.angular.z = diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
        self.pub_vel.publish(msg)
        
     
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()