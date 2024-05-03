from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,TimerAction,RegisterEventHandler
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution,Command
from launch_ros.actions import Node
from launch.event_handlers import OnProcessStart

def generate_launch_description():
    ld = LaunchDescription()




    rviz_config_file = PathJoinSubstitution([FindPackageShare('ezmower_robot'),'config','robot.rviz'])

    action_launch_rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time' : False}]
    )
    



    ld.add_action(action_launch_rviz)
    return ld
