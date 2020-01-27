#!/usr/bin/env python
###受信するプログラム

###ライブラリを持ってくる
import rospy
from std_msgs.msg import String

def string_check(msg):
    if msg.data == '0' :###もし、0と入力されたら
        print("\rLED OFF")###モニターに出力
    elif msg.data == '1' :###もし、１と入力されたら
        print("\rLED ON")###モニターに出力


if __name__ == "__main__":
    rospy.init_node("led_sub")###ここで受け取る
    sub = rospy.Subscriber('led_flash_str', String, string_check)###string_checkここで関数を呼ぶ
    rospy.spin()
