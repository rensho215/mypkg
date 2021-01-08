#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0
m = 0

def cb(message):
    global n,m
    n = message.data*2
    m = message.data*3

if __name__ == '__main__':
    rospy.init_node('two-three')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('two-three', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        pub.publish(m)
        rate.sleep()
