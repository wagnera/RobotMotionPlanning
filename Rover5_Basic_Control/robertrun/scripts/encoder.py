#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import quadrature_v2
from sensor_msgs.msg import JointState
import rospy
import roslib

class encoder_reader:
	def __init__(self):
		GPIO.setup("P9_30", GPIO.IN)#Left Encoder State A
		GPIO.setup("P9_23", GPIO.IN)#Left Encoder State B
		GPIO.setup("P8_26", GPIO.IN)#Right Encoder State A
		GPIO.setup("P8_17", GPIO.IN)#Right Encoder State B
		
		self._encoder_leftA_state = None
		self._encoder_leftB_state = None
		self._encoder_rightA_state = None
		self._encoder_rightB_state = None
		
	def read(self):
		self._encoder_leftA_state = GPIO.input("P9_30")
		self._encoder_leftB_state = GPIO.input("P9_23")
		self._encoder_rightA_state = GPIO.input("P8_26")
		self._encoder_rightB_state = GPIO.input("P8_17")
		
	#def publish(data):
	@property
  	def encoder_leftA_state(self):
  		return self._encoder_leftA_state
  	@property
  	def encoder_leftB_state(self):
  		return self._encoder_leftB_state
  	@property
  	def encoder_rightA_state(self):
  		return self._encoder_rightA_state
  	@property
  	def encoder_rightB_state(self):
  		return self._encoder_rightB_state
if __name__ == '__main__':
	QuadUpdate = encoder_reader()#creating instance of encoder_reader class 
	QuadEstimate_Left = quadrature_v2.QuadratureEstimator()
	QuadEstimate_Right = quadrature_v2.QuadratureEstimator()

	try:
		#Initialize node
		rospy.init_node('encoder_read')
		print "printng encoder_read"
		rate = rospy.Rate(2000)
		print "setrate"
		FLW_pub = rospy.Publisher('py_controller/front_left_wheel/encoder', JointState, queue_size=10)
		FRW_pub = rospy.Publisher('py_controller/front_right_wheel/encoder', JointState, queue_size=10)
		RLW_pub = rospy.Publisher('py_controller/back_left_wheel/encoder', JointState, queue_size=10)
		RRW_pub = rospy.Publisher('py_controller/back_right_wheel/encoder', JointState, queue_size=10)
		print "publishers set"
		FR = JointState()
		FL = JointState()
		RR = JointState()
		RL = JointState()
		print "messages created"
		while not rospy.is_shutdown():
			print "inside while not"
			QuadUpdate.read() #calling update to pins
			QuadEstimate_Left.update(QuadUpdate.encoder_leftA_state,QuadUpdate.encoder_leftB_state,rospy.get_time())
			QuadEstimate_Right.update(QuadUpdate.encoder_rightA_state,QuadUpdate.encoder_rightB_state,rospy.get_time())
			FL.velocity = [QuadEstimate_Left.velocity]#add velocity data to message
			RL.velocity = [QuadEstimate_Left.velocity]
			FR.velocity = [QuadEstimate_Left.velocity]
			RR.velocity = [QuadEstimate_Left.velocity]
			FL.position = [QuadEstimate_Left.position]#add position data to message
			RL.position = [QuadEstimate_Left.position]
			FR.position = [QuadEstimate_Left.position]
			RR.position = [QuadEstimate_Left.position]
			print "classes created"
			try:
				FLW_pub.publish(FL) #publish msg to joint_state
				FRW_pub.publish(FR)
				RLW_pub.publish(RL)
				RRW_pub.publish(RR) 
				print "publishing"
			except rospy.ROSInterruptException:
				pass
			rate.sleep()
	except:
		pass