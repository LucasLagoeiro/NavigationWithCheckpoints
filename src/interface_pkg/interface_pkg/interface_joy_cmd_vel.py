import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3

import json
from os import path


class Interface_JOY_CMDVEL(Node):

    def __init__(self):
        super().__init__('Interface_JOY_CMDVEL')
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(Twist,'cmd_vel',10)
        self.publisher

    def listener_callback(self, msg):
        # self.get_logger().info('I heard: "%s"' % msg.axes[0]) # esquerda direita analogico esquerdo
        self.left_right = msg.axes[0]
        self.get_logger().info('I heard: "%s"' % msg.axes[1]) # frente tras analogico esquerdo
        self.foward_back = msg.axes[1]
        # self.get_logger().info('I heard: "%s"' % msg.axes[5])

        self.ir_para_frente = Twist(linear=Vector3(x= 0.1,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))
        self.ir_para_tras   = Twist(linear=Vector3(x=-0.1,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))
        self.girar_direita  = Twist(linear=Vector3(x= 0.0,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z=-0.2))
        self.girar_esquerda = Twist(linear=Vector3(x= 0.0,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.2))
        self.parar          = Twist(linear=Vector3(x= 0.0,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))

        if self.left_right > 0.5: self.publisher.publish(self.girar_esquerda)
        elif self.left_right < -0.5: self.publisher.publish(self.girar_direita)
        elif self.foward_back > 0.5: self.publisher.publish(self.ir_para_frente)
        elif self.foward_back < -0.5: self.publisher.publish(self.ir_para_tras)
        else: self.publisher.publish(self.parar)

        # if self.foward_back > 0.5: self.publisher.publish(self.ir_para_frente)
        # elif self.foward_back < -0.5: self.publisher.publish(self.ir_para_tras)
        # else: self.publisher.publish(self.parar)
            
        
        











def main(args=None):
    rclpy.init(args=args)
    interface_JOY_CMDVEL = Interface_JOY_CMDVEL()
    rclpy.spin(interface_JOY_CMDVEL)
    interface_JOY_CMDVEL.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()