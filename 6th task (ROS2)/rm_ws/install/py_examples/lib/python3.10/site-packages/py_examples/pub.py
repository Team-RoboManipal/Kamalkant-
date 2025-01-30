import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class PublisherNode(Node):
    def __init__(self):
        super().__init__("Publisher")
        self.count=0
        self.publisher_=self.create_publisher(String,"/message",10)
        self.timer_=self.create_timer(0.5,callback=self.callback)
    def callback(self):
        msg=String()
        msg.data=f"Message:{self.count}"
        self.get_logger().info(msg.data)
        self.count+=1
        self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node=PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()