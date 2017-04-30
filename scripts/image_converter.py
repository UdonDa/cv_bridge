#!/usr/bin/env python
# coding: utf-8

import sys, rospy, cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#from __future__ import print_function
#from __future__ import print_function

# class 
class image_converter:

    def __init__(self):
        self.image_pub = rospy.Publisher("image_topic_2", Image, queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("Image_topic", Image, self.callback)

    # 
    def callback(self,data):
        
        # imgmsg_to_cv2を使うときはtry-catchを使おう！
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print e

        (rows, cols, channels) = cv_image.shape
        if cols > 60 and rows > 60:
            cv2.circle(cv_image, (50,50), 10, 255)

        cv2.imshow("Image windows", cv_image)
        cv2.waitKey(3)

        try:
            # ROSのイメージフォーマットは、bgr8
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
            
            ###--- OpenCV-image to ROS-Message
            #self.image_pun.publish(self.bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
        except CvBridgeError as e:
            print e

def main(args):
    ic = image_converter()

    # rospyが固有のノードを持つように、anonumous=True
    rospy.init_node('image_converter', anonymous=True)

    # ノードが終わるまでの間、rospy.spin()が↑ のノードを終わらせんようにする
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    #がぞーとじる
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)




















