import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallFollower(Node):
    def __init__(self):
        super().__init__('wall_follower') 
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription=self.create_subscription(LaserScan,'/scan',self.read_scan_data,10)
        self.timer = self.create_timer(0.1, self.publish_cmd_vel)
        self.linear_vel = 0.01
        self.regions={'region1':100, 'region2':100, 'region3':100}
        self.velocity=Twist()


    def read_scan_data(self,scan_data):
 
        self.regions = {
        'region1':   min(min(scan_data.ranges[0:20]), 100),
        'region2':   min(min(scan_data.ranges[20:40]), 100),
        'region3':   min(min(scan_data.ranges[40:90]), 100)
        }
        print(self.regions['region1'], "    ", self.regions['region2'], "     ", self.regions['region3'])

  
    def publish_cmd_vel(self):
        self.velocity.linear.x = self.linear_vel
        # TODO
        # Compare scan data of various regions and change the direction 
        # of robot
        self.publisher.publish(self.velocity)
        

def main(args=None):
    rclpy.init(args=args)
    node=WallFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()