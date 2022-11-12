from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf = '/home/manyu/ros2_ws/src/lab4/urdf/four_wheeled_robot.urdf'
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf]),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            arguments=[urdf]),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'),  
    ])