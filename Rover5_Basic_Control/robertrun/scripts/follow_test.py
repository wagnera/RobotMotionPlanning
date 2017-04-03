#!/usr/bin/python
#This script takes input from the pololu ir sensor and uses that to locate another robot
#This information is used to direct the robot to follow the other robot

import Adafruit_BBIO.GPIO as GPIO
from geometry_msgs .msg import Twist
import rospy
import roslib

class followR(): #create class for following robot
        def __init__(self):
                GPIO.setup("P9_24", GPIO.IN)#North state
                print "P9_24 setup"
                GPIO.setup("P9_27", GPIO.IN)#East
                print "P9_26 setup"
                GPIO.setup("P9_41", GPIO.IN)#South
                print "P9_27 setup"
                GPIO.setup("P9_26", GPIO.IN)#West
                print "P9_41 setup"
                self._north_state = None
                self._east_state = None
                self._south_state = None
                self._west_state = None

        def read(self):
                self._north_state = GPIO.input("P9_24")
                self._east_state = GPIO.input("P9_27")
                self._south_state = GPIO.input("P9_41")
                self._west_state = GPIO.input("P9_26")

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
    cmdpub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    cmdvel = Twist()
    rate = rospy.Rate(10) # set rospy rate to 5Hz
    while not rospy.is_shutdown():
        FollowRobot.read()
        if FollowRobot.south_state == 0:
		cmdvel.linear.x = 0.2
        	cmdvel.angular.z = 0
		print "south"
	if FollowRobot.north_state == 0:
                cmdvel.linear.x = -0.2
		cmdvel.angular.z = 0
		print "north"
        if FollowRobot.east_state == 0:
                cmdvel.linear.x = 0
        	cmdvel.angular.z = 3
		print "east"
	if FollowRobot.west_state == 0:
                cmdvel.linear.x = 0
		cmdvel.angular.z =-3
		print "west"
        #if north_state
	try:
        	cmdpub.publish(cmdvel)
    	except rospy.ROSInterruptException:
		pass
    #We need to wait for new messages
    	rate.sleep()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
 
