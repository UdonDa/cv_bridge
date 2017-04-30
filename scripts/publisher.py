#!/usr/bin/env python
# encoding: utf-8
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

#def publisher():
pub = rospy.Publisher('Image_topic', Image, queue_size=10)
rospy.init_node('publisher', anonymous=True)
    
    # 1Hz
r=rospy.Rate(10)
#print "aaa"

#ぶりっじかく
bridge = CvBridge()

while not rospy.is_shutdown():
        

##cv→　rosメッセージのイメージ型にする
    pic = cv2.imread('./sagiri.jpg')

    cv_image = bridge.cv2_to_imgmsg(pic, "bgr8")

    rospy.loginfo(cv_image)
    pub.publish(cv_image)
    r.sleep()

"""
if __name__ == '__name__':
    try:
        print "aaa"
        publisher()
    except rospy.ROSInterruptException:
        pass
"""
