#!/usr/bin/env python
###送信プログラム###

###ライブラリを持ってくる###
import roslib
import rospy
import time
import wiringpi
import subprocess
from std_msgs.msg import String

#main
if __name__ == '__main__':
    ### 14(ラズパイの8番)と17（ラズパイの11番）の二つのピンを使えるようにする###
    subprocess.check_call('gpio export 14 out',shell=True)
    subprocess.check_call('gpio export 17 out',shell=True)
    ###
    rospy.init_node('led_pub')

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
    io.pinMode(14,io.OUTPUT)  # ピン番号８番に出力ピンと教える
    io.pinMode(17,io.OUTPUT)  # ピン番号11番に出力ピンと教える

   ###周り続ける
    while not rospy.is_shutdown():
        i = raw_input()###入力を受け付ける。プログラムが入力待ちになる
        pub = rospy.Publisher('led_flash_str', String, queue_size=1)
        pub.publish(i)

        if i == '0' :
            io.digitalWrite(14,0) ###8番のピンの光を消す
            io.digitalWrite(17,0)###11番のピンの光を消す
            time.sleep(1)###スリープ
            
        elif i == '1' :
            io.digitalWrite(14,1)###8番のピンを光らせる
            io.digitalWrite(17,1)###11番のピンを光らせる
            time.sleep(1)###スリープ
        else :
            io.digitalWrite(14,0)###それ以外の時
            io.digitalWrite(17,0)
            time.sleep(1)
