import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys
class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.cli_=self.create_client(AddTwoInts,"add_two_ints")
        while not self.cli_.wait_for_service(timeout_sec=1):
            self.get_logger().info("Waiting For Service")
        self.req=AddTwoInts.Request()
    def send_req(self,a,b):
        self.req.a=a
        self.req.b=b
        return self.cli_.call_async(self.req)
def main(args=None):
    rclpy.init()
    node=Client()
    future=node.send_req(int(sys.argv[1]),int(sys.argv[2]))
    rclpy.spin_until_future_complete(node,future)
    node.get_logger().info(f'{sys.argv[1]}+{sys.argv[2]}={future.result().sum}')
    node.destroy_node()
    rclpy.shutdown()