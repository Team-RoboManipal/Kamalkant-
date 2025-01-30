import rclpy
from rclpy.node import Node
import sys
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
class GOAL_NODE(Node):
    def __init__(self):
        super().__init__("GOAL")
        if len(sys.argv) != 3 :
            self.get_logger().error("Usage: ros2 run <pkg_name> goal X Y")
            sys.exit(1)

        self.goal_x = float(sys.argv[1])
        self.goal_y = float(sys.argv[2])
        self.tolerance=1.5
        self.linear_constant=1.5
        self.angular_constant=6

        self.get_logger().info(f"Going to goal: X={self.goal_x}, Y={self.goal_y}")
        self.subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.pose = None  
        self.pose = None
        self.reached_goal = False

    def pose_callback(self, pose):
        if not self.reached_goal:
            if self.distance(pose) <= self.tolerance:
                self.reached_goal = True
                self.get_logger().info("Goal reached!")
            else:
                self.msg(self.linear_velocity(pose), 0, self.angular_vel(pose))


    def linear_velocity(self,pose):
        return self.linear_constant*self.distance(pose)
    
    def angular_vel(self, pose: Pose):
        angle_to_goal = math.atan2(self.goal_y - pose.y, self.goal_x - pose.x)
        angle_diff = angle_to_goal - pose.theta
        return self.angular_constant * angle_diff

    def distance(self,pose : Pose):
        return math.sqrt((pose.x-self.goal_x)**2+(pose.y-self.goal_y)**2)
    
    def msg(self,x,y,z):
        msg=Twist()
        msg.linear.x=float(x)
        msg.linear.y=float(y)
        msg.angular.z=float(z)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=GOAL_NODE()
    rclpy.spin(node)
    if node.reached_goal:
        node.destroy_node()
        rclpy.shutdown()