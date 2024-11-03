import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseWithCovarianceStamped

import json
from os import path


class saveCheckpoints(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'amcl_pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # self.get_logger().info('I heard: "%s"' % msg.pose.pose.position)
        mcl_p = msg.pose.pose.position
        mcl_q = msg.pose.pose.orientation

        p_x = mcl_p.x
        p_y = mcl_p.y

        q_x = mcl_q.x        
        q_y = mcl_q.y
        q_z = mcl_q.z
        q_w = mcl_q.w


        self.get_logger().info(f'I heard posX: "{p_x}", posY: {p_y}')

        filename = '/home/llagoeiro/Desktop/FEI/8_semestre/RoboticaProbFolder/proj3/TurtleBot3/src/navigation_pkg/map/checkpoints.json'
        dictObj = []
        
        # Check if file exists
        if path.isfile(filename) is False:
            raise Exception("File not found")
        
        # Read JSON file
        with open(filename) as fp:
            dictObj = json.load(fp)

        # Append new pose data
        new_pose = {
            "position": {"x": round(p_x,2), "y": round(p_y,2), "z": 0.0},
            "orientation": {"x": round(q_x,2), "y": round(q_y,2), "z": round(q_z,2), "w": round(q_w,2)}
        }        

        dictObj["poses"].append(new_pose)
        
        self.get_logger().info(str(dictObj))


        with open(filename, 'w') as json_file:
            json.dump(dictObj, json_file, indent=4)
        
                
        # self.get_logger().info(str(dictObj))







def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = saveCheckpoints()
    rclpy.spin_once(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()