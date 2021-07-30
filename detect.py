#!/usr/bin/env python

## Simple node that publishes the detected objects in std_msgs/Strings messages
## to the 'object_detector' topic

# cp ../exchange/* ./
# rosrun object_detection detect.py

import rospy
from std_msgs.msg import String
import os

def detect():
    largest_id = 0
    largest_image_name = ""
    pub = rospy.Publisher('object_detector', String, queue_size=10)
    rospy.init_node('detect', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        file_list = os.listdir("/home/user/ws")
        #os.system("rosrun image_view image_saver image:=\"/xtion/rgb/image_rect_color\"")
        for image in file_list:
            if ".jpg" in image:
                image_name = image
                #get the number ID of the image
                image_id = image_name.replace("left", "")
                image_id = image_id.replace(".jpg", "")
                image_id = int(image_id)
                if image_id > largest_id:
                    largest_id = image_id
                    largest_image_name = image_name
        rospy.loginfo(largest_image_name)
        pub.publish(largest_image_name)
        rate.sleep()

if __name__ == '__main__':
    try:
        detect()
    except rospy.ROSInterruptException:
        pass
