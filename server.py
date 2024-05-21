import rclpy
from classController import Controller
from geometry_msgs.msg import Twist
import sys, tty, termios
from collections import deque
import time


def keypress(sett):
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, sett)
    return key

if __name__ == '__main__':    
    dq = deque()
    rclpy.init()
    cont = Controller()
    print("Use 'w','a','s' e 'd' para mover o robo ou 'q' para desconetar\n")
    orig_settings = termios.tcgetattr(sys.stdin)

    tty.setcbreak(sys.stdin)
    x = 0
    hasStoped = False
    while True: 
        x=sys.stdin.read(1)[0]
        if x == 'w' or x == "a" or x == "s" or x == "d":
            cont.move(x)
        elif x == "q" and hasStoped:
            rclpy.shutdown()
            break
        elif x == "q" and not hasStoped:
            print("Pressione 'e' para controlar o robo e 'q' para fechar\n")
            hasStoped = True
            cont = None
        elif x == "e" and hasStoped:
            hasStoped = False
            cont = Controller()
            print("Use 'w','a','s' e 'd' para mover o robo ou 'q' para desconetar \n ")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
