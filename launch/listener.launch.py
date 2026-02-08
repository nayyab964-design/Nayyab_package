from launch import LaunchDescription
from launch_ros.actions import node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_noodes_py',
            executable='listener'
                )
    ])