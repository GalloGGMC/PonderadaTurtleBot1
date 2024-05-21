import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def move(self,key : str):
        msg = Twist()
        match(key.lower()):
            case 'w':
                msg = self.go(msg)
            case 's':
                msg = self.reverse(msg)
            case 'a':
                msg = self.left(msg)
            case 'd':
                msg = self.right(msg)
            case 'q':
                msg = self.stop(msg)
        self.publisher.publish(msg)
    
    def left(self,msg):
        msg.linear.x = 0.0
        msg.angular.z = 0.785
        return msg
    
    def right(self,msg):
        msg.linear.x = 0.0
        msg.angular.z = -0.785
        return msg
    
    def go(self,msg):
        msg.linear.x = 0.2
        msg.angular.z = 0.0
        return msg
    
    def reverse(self,msg):
        msg.linear.x = -0.2
        msg.angular.z = 0.0
        return msg
    
    def stop(self,msg):
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        return msg

if __name__ == "__main__":
    rclpy.init()

    col = Controller("w")
    rclpy.spin(col)

    rclpy.shutdown()
    
        