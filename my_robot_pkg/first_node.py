#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class First_node(Node):
    def  __init__(self):
        super(). __init__("first_node")
        self.create_timer(1.0,self.timer_callback)
        self.counter=0
    def timer_callback(self):
        self.get_logger().info("helllo first node"+str(self.counter))
        self.counter+=1

def main(args=None):
    rclpy.init(args=args)
    node=First_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
