#!/usr/bin/env python3
# license removed for brevity
import rospy
from tuto.msg import aer

def talker():
    pub = rospy.Publisher('/rosout', aer, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = aer()
        aer.data=
        aer.score=
        aer.time=
        #msg = Twist()
        #msg.linear.x = 1.0
        #msg.linear.y = 0.0
        #msg.linear.z = 0.0
        #msg.angular.x = 0.0
        #msg.angular.y = 0.0
        #msg.angular.z = 5.0

        #rospy.loginfo(hello_str)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

