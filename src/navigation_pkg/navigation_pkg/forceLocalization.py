import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty
from rclpy.timer import Timer

class RequestPoseUpdate(Node):
    def __init__(self):
        super().__init__('request_pose_update')
        self.publisher = self.create_publisher(Empty, '/request_nomotion_update', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Atualiza a cada segundo

    def timer_callback(self):
        msg = Empty()
        self.publisher.publish(msg)
        self.get_logger().info("Forçando atualização da posição pelo amcl")

def main(args=None):
    rclpy.init(args=args)
    node = RequestPoseUpdate()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()