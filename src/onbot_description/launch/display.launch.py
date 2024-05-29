from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
        
        
        
                
        use_sim_time = LaunchConfiguration('use_sim_time', default='false')

        urdf_file_name = 'robot.urdf'
        urdf = os.path.join(
                get_package_share_directory('onbot_description'),
                "urdf",
                urdf_file_name)
        with open(urdf, 'r') as infp:
                robot_desc = infp.read()

        robot_state_publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf]
        )
        
        joint_state_publisher_gui = Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui"
        )
        
        rviz_node = Node(
                package="rviz2",
                executable="rviz2",
                name="rvzi2",
                output="screen",
                arguments=["-d", os.path.join(get_package_share_directory("onbot_description"), "rviz", "display.rviz")] 
        )
        
        
        return LaunchDescription([
                robot_state_publisher,
                joint_state_publisher_gui,
                rviz_node
        ])
        

