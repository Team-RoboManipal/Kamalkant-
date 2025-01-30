import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class Server(Node):
    def __init__(self):
        super().__init__('Serivce')
        self.server_=self.create_service(AddTwoInts,"add_two_ints",self.callback)

    def callback(self,request,response):
        response.sum = request.a +request.b
        self.get_logger().info(f"Incoming Request a:{request.a}+b:{request.b}")
        return response


def main(args=None):
    rclpy.init()
    node=Server()
    rclpy.spin(node=node)
    rclpy.shutdown()