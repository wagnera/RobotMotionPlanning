#!/usr/bin/python
import time
import Adafruit_BBIO.GPIO as GPIO
from geometry_msgs .msg import Twist
import rospy
import roslib


if __name__ == '__main__':

  #Robert.__init__()
  try:
    #Initialize node
    rospy.init_node('follow')
    cmdpub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    cmdvel = Twist()
    rate = rospy.Rate(10) # set rospy rate to 5Hz
    while not rospy.is_shutdown():
	
	cmdvel.linear.x = 0.2
       	cmdvel.angular.z = 0
	print "south"
	time.sleep(5)
        cmdvel.linear.x = -0.2
	cmdvel.angular.z = 0
	print "north"
	time.sleep(5)
        cmdvel.linear.x = 0
        cmdvel.angular.z = 3
	print "east"
	time.sleep(1)
        cmdvel.linear.x = 0
	cmdvel.angular.z =-3
	print "west"
	time.sleep(1)
	cmdvel.linear.x = 0
	cmdvel.angular.z = 0
	time.sleep(5)
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
