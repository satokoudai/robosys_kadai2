#!/usr/bin/env python
import roslib
import rospy
import time
import wiringpi
import subprocess
from std_msgs.msg import String

#main
if __name__ == '__main__':
    ### init io port ###
    subprocess.check_call('gpio export 14 out',shell=True)
    subprocess.check_call('gpio export 17 out',shell=True)
    ###
    rospy.init_node('led_pub')

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
    io.pinMode(14,io.OUTPUT)  # Setup pin 11
    io.pinMode(17,io.OUTPUT)  # Setup pin 8

    while not rospy.is_shutdown():
        i = raw_input()
        pub = rospy.Publisher('led_flash_str', String, queue_size=1)
        pub.publish(i)

        if i == '0' :
            io.digitalWrite(14,0)
            io.digitalWrite(17,0)
            time.sleep(1)
        elif i == '1' :
            io.digitalWrite(14,1)
            io.digitalWrite(17,1)
            time.sleep(1)
        else :
            io.digitalWrite(14,0)
            io.digitalWrite(17,0)
            time.sleep(1)
