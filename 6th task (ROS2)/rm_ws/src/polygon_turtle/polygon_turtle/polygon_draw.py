import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
 # type: ignore
from tutorial_interfaces.srv import NSides

class PolygonNode(Node):
    def __init__(self):
        super().__init__("Draw_polygon")
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.server_=self.create_service(NSides,"Polygon",self.callback)
        self.get_logger().info("Polygon node has been started")

    def callback(self,request,response):
        n=request.n
        self.draw_polygon(n, 2)
        
    def draw_polygon(self, n, side_length):
        self.exterior_angle = math.radians(360 / n)
        self.get_logger().info(f"Drawing polygon with {n} sides, each of length {side_length}")

        for i in range(n):
            self.get_logger().info(f"Drawing side {i + 1}")
            for j in range(int(side_length)):
                self.msg(1, 0, 0)  # Move forward
                self.get_logger().info(f"Moving forward step {j + 1}")
                rclpy.spin_once(self, timeout_sec=1)  # Sleep for 1 second
            self.msg(0, 0, self.exterior_angle)  # Rotate
            self.get_logger().info(f"Rotating by {self.exterior_angle} radians")
            rclpy.spin_once(self, timeout_sec=2)  # Sleep for 1 second

    def msg(self, x, y, z):
        msg = Twist()
        msg.linear.x = float(x)
        msg.linear.y = float(y)
        msg.angular.z = float(z)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published message: linear.x={x}, linear.y={y}, angular.z={z}")

def main(args=None):
    rclpy.init(args=args)
    node = PolygonNode()
    rclpy.spin(node)
    rclpy.shutdown()