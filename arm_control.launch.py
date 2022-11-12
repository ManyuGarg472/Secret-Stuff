import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from scripts import GazeboRosPaths

def generate_launch_description():
    urdf_file = '/home/manyu/ros2_ws/src/lab5/urdf/manipulator.urdf'    
    controller_file = '/home/manyu/ros2_ws/src/lab5/config/control.yaml'
    robot_description = {"robot_description": urdf_file}
    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","-s","libgazebo_ros_factory.so",],
                output="screen",
            ),
            Node(
                package="gazebo_ros",
                node_executable="spawn_entity.py",
                arguments=["-entity","lab5","-b","-file", urdf_file],
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                arguments=[urdf_file],
            ),
            
            Node(
                package="controller_manager",
                executable="ros2_control_node",
                parameters=[robot_description, controller_file],
                output={
                    "stdout": "screen",
                    "stderr": "screen",
                },
            ),
            Node(
            package="controller_manager",
            executable="spawner.py",
            arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
                ),

            Node(
                package="controller_manager",
                executable="spawner.py",
                arguments=["joint_trajectory_controller", "-c", "/controller_manager"],
            )
        ]
    )