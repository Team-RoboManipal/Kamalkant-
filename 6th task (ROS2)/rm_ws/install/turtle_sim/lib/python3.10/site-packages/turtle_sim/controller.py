import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import sys, termios, tty

class controle_node(Node):
    def __init__(self):
        super().__init__("Controller",)
        self.publisher_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.print_instructions()
        self.timer = self.create_timer(0.1, self.check_key)

    def check_key(self):
        key = self.get_key()
        if key:
            self.redirect(key)

    def redirect(self, key):
        if key == "w":
            self.msg(1.0, 0.0, 0.0)
        elif key == "s":
            self.msg(-1.0, 0.0, 0.0)
        elif key == "a":
            self.msg(0.0, 0.0, 1.0)
        elif key == "d":
            self.msg(0.0, 0.0, -1.0)
        elif key == "q":
            self.get_logger().info("Exiting...")
            rclpy.shutdown()

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            termios.tcsetattr(fd, termios.TCSANOW, termios.tcgetattr(fd))  # Set noecho mode
            key = sys.stdin.read(1)  # Read single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore original settings
        return key
    
    def msg(self,x,y,z):
        msg=Twist()
        msg.linear.x=x
        msg.linear.y=y
        msg.angular.z=z
        self.publisher_.publish(msg)

    def print_instructions(self):
        instructions = """
        Welcome to Turtle Controller!
        
        Use the following keys to control the turtle:
        - 'w' : Move forward
        - 's' : Move backward
        - 'a' : Rotate counterclockwise
        - 'd' : Rotate clockwise
        - 'q' : Quit the program
        
        Press any of the above keys to start controlling the turtle.
        """
        self.get_logger().info(instructions)




def main(args=None):
    rclpy.init(args=args)
    node=controle_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()