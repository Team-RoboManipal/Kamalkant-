import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class PublisherNode(Node):
    def __init__(self):
        super().__init__("Publisher")
        self.subscriber_=self.create_subscription(String,"/message",callback=self.callback,qos_profile=10)
    def callback(self,msg: String):
        self.get_logger().info(msg.data)
def main(args=None):
    rclpy.init(args=args)
    node=PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()