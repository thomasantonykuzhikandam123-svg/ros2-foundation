# ROS2 Foundations

Learning ROS2 Humble from scratch as part of my self-learning journey 
towards becoming a Robotics Engineer.

Built while studying for RMIT Masters in Robotics and Mechatronics, 
graduating November 2026.

## What I built and how I learned

### first_node.py
My very first ROS2 node written completely from scratch from memory.

What it does: prints "hello" with an incrementing counter every second.

Concepts learned:
- How a ROS2 node is a Python class inheriting from Node
- create_timer() — runs a function every X seconds
- get_logger().info() — ROS2 logging
- rclpy.spin() — keeps node running

How I ran it:
ros2 run my_robot_pkg first_node

### draw_circle.py
Publisher node that makes a turtle draw a circle in turtlesim.

What it does: continuously publishes velocity commands to /turtle1/cmd_vel
causing the turtle to move in a circle.

Concepts learned:
- create_publisher() — publishing messages to a topic
- Twist message type from geometry_msgs
- linear.x controls forward speed
- angular.z controls turning speed
- A circle needs both at the same time

How I ran it:
Terminal 1: ros2 run turtlesim turtlesim_node
Terminal 2: ros2 run my_robot_pkg draw_circle

### pose_subscriber.py
Subscriber node that reads and prints the turtle's position.

What it does: subscribes to /turtle1/pose and logs x, y, theta 
every time the turtle moves.

Concepts learned:
- create_subscription() — subscribing to a topic
- Pose message type from turtlesim.msg
- Subscriber callback receives message automatically from ROS2
- No timer needed — callback fires when message arrives

How I ran it:
Terminal 1: ros2 run turtlesim turtlesim_node
Terminal 2: ros2 run turtlesim turtle_teleop_key
Terminal 3: ros2 run my_robot_pkg pose_subscriber

### turtle_controller.py
My most complex node — combines publisher, subscriber and service call.

What it does:
- Turtle moves forward in open space
- Turns when it gets near the walls
- Pen turns RED when turtle crosses x=5.5 going right
- Pen turns GREEN when turtle crosses x=5.5 going left

Concepts learned:
- Combining publisher and subscriber in one node
- Wall detection using pose.x and pose.y conditions
- Service calls using create_client() and call_async()
- Async callbacks using future and add_done_callback()
- functools.partial for callback arguments
- previous_x_ variable to detect direction of crossing

How I ran it:
Terminal 1: ros2 run turtlesim turtlesim_node
Terminal 2: ros2 run my_robot_pkg turtle_controller

## Workspace setup commands

# Create workspace
mkdir -p ~/robot_ws2/src
cd ~/robot_ws2/src

# Create package
ros2 pkg create --build-type ament_python my_robot_pkg --dependencies rclpy

# Create a node
cd my_robot_pkg/my_robot_pkg
touch node_name.py
chmod +x node_name.py

# Add to setup.py entry_points:
'node_name = my_robot_pkg.node_name:main'

# Build
cd ~/robot_ws2
colcon build --symlink-install
source install/setup.bash

# Run
ros2 run my_robot_pkg node_name

## Built as part of
RMIT Masters in Robotics and Mechatronics — May 2026
