#!/usr/bin/python
#This script takes input from the pololu ir sensor and uses that to locate another robot
#This information is used to direct the robot to follow the other robot

import Adafruit_BBIO.GPIO as GPIO
from geometry_msgs .msg import Twist
import rospy
import roslib

class followR(self, data): #create class for following robot
	def __init__(self):
		GPIO.setup("P9_24", GPIO.IN)#North state
		GPIO.setup("P9_26", GPIO.IN)#East
		GPIO.setup("P9_27", GPIO.IN)#South
		GPIO.setup("P9_41", GPIO.IN)#West
		
		self._north_state = None
		self._east_state = None
		self._south_state = None
		self._west_state = None
		
	def read(self):
		self._north_state = GPIO.input("P9_30")
		self._east_state = GPIO.input("P9_23")
		self._south_state = GPIO.input("P8_26")
		self._west_state = GPIO.input("P8_17")
	
	#def publish(data):
	@property
  	def north_state(self):
  		return self._north_state
  	@property
  	def east_state(self):
  		return self._east_state
  	@property
  	def south_state(self):
  		return self._south_state
  	@property
  	def west_state(self):
  		return self._west_state
  


# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  FollowRobot=followR()
  #Robert.__init__()
  try:
    #Initialize node
    rospy.init_node('follow')
       
    
    rate = rospy.Rate(5) # set rospy rate to 5Hz
    while not rospy.is_shutdown():
    	FollowRobot.read()
    	print FollowRobot.south_state
    	if north_state

    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass

