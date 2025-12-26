import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    scanner = launch_ros.actions.Node(
            package='register',
            executable='scanner',
            name='scanner',
            output='screen',
            prefix='xterm -e'
            )

    display = launch_ros.actions.Node(
            package='register',
            executable='display',
            name='display',
            output='screen',
            )

    return launch.LaunchDescription([display, scanner])
