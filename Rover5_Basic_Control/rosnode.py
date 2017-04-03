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
def callback(data):
   # create an instance of the quadrature estimator class
    
    if data.header.stamp.nsecs !=0:
      TestTime = ((data.header.stamp.nsecs) * (10 ** -9))
    else:
      TestTime = 0
    #update the program
    QuadEdit.update(data.state_a.data,data.state_b.data,(TestTime + data.header.stamp.secs)) 
    
#publish on topic /joint_out
def echo():
 	#create subscriber that subscribes to the /ticks topic and uses the callback function
  rospy.Subscriber("ticks", Quadrature, callback)
  #create the published which publishes to /joint_out with msg type of JointState
  pub = rospy.Publisher('joint_out', JointState, queue_size=100)
  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    #call subscriber
    rospy.Subscriber("ticks", Quadrature, callback)
    outmsg = JointState() #create a msg of type JointState
    outmsg.name = "Quadrature" #define name of the JointState
    outmsg.position = QuadEdit.position #set position to calculated position from update function of QuadEdit class
    outmsg.velocity = QuadEdit.velocity #same as above but for velocity
    #print outmsg DEBUG
    try:
      pub.publish(outmsg) #publish msg to joint_state ONLY PROBLEM IN CODE
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