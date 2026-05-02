#!usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose
class Pose_subscriber(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.create_subscription(Pose ,"/turtle1/pose",self.pos_callback,10)
    def pos_callback(self, pos:Pose):
        self.get_logger().info(f"x: {pos.x}, y:{pos.y}, theta:{pos.theta}")
def main(args=None):
    rclpy.init(args=args)
    node=Pose_subscriber()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()