#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def string_check(msg):
    if msg.data == '0' :
        print("\rLED OFF")
    elif msg.data == '1' :
        print("\rLED ON")


if __name__ == "__main__":
    rospy.init_node("led_sub")
    sub = rospy.Subscriber('led_flash_str', String, string_check)
    rospy.spin()
