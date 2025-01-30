import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class DrawNode(Node):
    def __init__(self):
        super().__init__("DrawCircle")
        #self.subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.1,self.draw_d)
        self.start_time = self.get_clock().now()
        self.r=2
        self.state = 'semicircle'
        self.line_length = 4

    def draw_d(self):
        current_time = self.get_clock().now()
        time_elapsed = (current_time - self.start_time).nanoseconds / 1e9
        
        if self.state == 'semicircle':
            if time_elapsed < math.pi:  # Time for a half-circle (180 degrees)
                self.msg(self.r, 0, 1)  # Move forward while rotating
            else:
                self.state = 'turn'  # Transition to the turn phase
                self.start_time = self.get_clock().now()  # Reset the timer for the next phase
                self.msg(0, 0, 0)  # Stop after the semicircle

        elif self.state == 'turn':
            if time_elapsed < (math.pi / 2)+0.11:  # Rotate for 90 degrees (π/2 radians)
                self.msg(0, 0, 1)  # Rotate in place
            else:
                self.state = 'line'  # Transition to the line phase
                self.start_time = self.get_clock().now()  # Reset the timer
                self.msg(0, 0, 0)  # Stop after the turn

        elif self.state == 'line':
            if time_elapsed < self.line_length / self.r:  # Move straight for the line length
                self.msg(self.r, 0, 0)  # Move forward
            else:
                self.state = 'done'  # Finish the drawing
                self.msg(0, 0, 0)  # Stop

    def msg(self,x,y,z):
        msg=Twist()
        msg.linear.x=float(x)
        msg.linear.y=float(y)
        msg.angular.z=float(z)
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawNode()
    rclpy.spin(node)
    
