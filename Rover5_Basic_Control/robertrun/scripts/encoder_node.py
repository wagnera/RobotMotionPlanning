#!/usr/bin/env python

#THis code creates a node that subsribes to the messages coming from the rosbag play and is used 
#test the quadrature.py python code which calculates velocity and position from quadrature encoder data.
#This is then published on /joint_out 
import rospy
import roslib
import quadrature
from khan_msgs.msg import Quadrature
from sensor_msgs.msg import JointState
from std_msgs.msg import String
#from std_msgs.msg import String
def callback(data):
   # create an instance of the quadrature estimator class
    
    if data.header.stamp.nsecs !=0:
      TestTime = ((data.header.stamp.nsecs) * (10 ** -9))
    else:
      TestTime = 0
    #update the program
    QuadEdit.update(data.state_a.data,data.state_b.data,(TestTime + data.header.stamp.secs))
    QuadEdit.update(data.state_a.data,data.state_b.data,(TestTime + data.header.stamp.secs)) 
    
#publish on topic /joint_out
def echo():
 	#create subscriber that subscribes to the /ticks topic and uses the callback function
  FLW_sub = rospy.Subscriber('/py_controller/front_left_wheel/cmd', Quadrature, callback)
  FRW_sub = rospy.Subscriber('/py_controller/front_right_wheel/cmd', Quadrature, callback)  
  BLW_sub = rospy.Subscriber('/py_controller/back_left_wheel/cmd', Quadrature, callback)
  BRW_sub = rospy.Subscriber('/py_controller/back_right_wheel/cmd', Quadrature, callback)
  #create the published which publishes to /joint_out with msg type of JointState
  FLW_pub = rospy.Publisher('py_controller/front_left_wheel/encoder', JointState, queue_size=10)
  FRW_pub = rospy.Publisher('py_controller/front_right_wheel/encoder', JointState, queue_size=10)
  BLW_pub = rospy.Publisher('py_controller/back_left_wheel/encoder', JointState, queue_size=10)
  BRW_pub = rospy.Publisher('py_controller/back_right_wheel/encoder', JointState, queue_size=10)
  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    #call subscribers
    rospy.Subscriber('/py_controller/front_left_wheel/cmd', Quadrature, callback)
    rospy.Subscriber('/py_controller/front_right_wheel/cmd', Quadrature, callback)  
    rospy.Subscriber('/py_controller/back_left_wheel/cmd', Quadrature, callback)
    rospy.Subscriber('/py_controller/back_right_wheel/cmd', Quadrature, callback)
    
    FLW_pub = JointState() #create a msg of type JointState
    FRW_pub = JointState()
    BLW_pub = JointState()
    BRW_pub = JointState()
   
    FLW_pub.position = [QuadEdit]
    FRW_pub.position = [QuadEdit]
    BLW_pub.position = [QuadEdit]
    BRW_pub.position = [QuadEdit]


    outmsg.position = [QuadEdit.position] #set position to calculated position from update function of QuadEdit class
    outmsg.velocity = [QuadEdit.velocity] #same as above but for velocity
    #print QuadEdit.position #DEBUG
    try:
      pub.publish(outmsg) #publish msg to joint_state 
    except rospy.ROSInterruptException:
      pass
    rate.sleep()
  

if __name__ == '__main__':
  #create an instance of the QuadratureEstimator class
  QuadEdit=quadrature.QuadratureEstimator(40)
  #create the quad_encoder node
  rospy.init_node('quad_encoder', anonymous=True)
  #listener()
  try: 
  	echo()
  except rospy.ROSInterruptException:
  	pass