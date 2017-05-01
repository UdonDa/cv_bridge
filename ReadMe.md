how to use CvBridge() and tensorflow with ROS

1. start tensorflow with ROS (MNIST)
roscore
python tensorflow_with_ros.py image:=/cv_camera/image_raw
rosrun cv_camera cv_camera_node
rostopic echo /result

So, by CNN, you can recognize [1~9] numbers
plese show [1~9] numbers to camera(0)


2. how to show a picture
roscore 
python image_converter.py
python publisher.py

So, you can see a cute girl
