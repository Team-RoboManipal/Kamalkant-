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
        self.create_timer(0.1,self.draw_circle)
        self.start_time = self.get_clock().now()
        self.r=2

    def draw_circle(self):
        current_time=self.get_clock().now()
        time_ellapsed=(current_time-self.start_time).nanoseconds/1e9
        if time_ellapsed<2*math.pi:
            self.msg(self.r,0,1)
        else:
            self.msg(0,0,0)
            

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
    
