#!/usr/bin/env python3
# license removed for brevity
import rospy
from tuto.srv import aer, aerResponse

def handler(req):
     return aerResponse (req.a + req.b)
     
def talker():
    
    rospy.init_node('talker', anonymous=True)
    s = rospy.Service('add_two_ints', aer, handler)
    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
