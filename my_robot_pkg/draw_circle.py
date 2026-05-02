#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
class Draw_circle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub= self.create_publisher(Twist,"/turtle1/cmd_vel",10 )
        self.create_timer(0.1,self.timer_callback)
        self.get_logger().info("draw_circle node have started")
    
    def timer_callback(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=4.0
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=Draw_circle()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__==main:
    main()