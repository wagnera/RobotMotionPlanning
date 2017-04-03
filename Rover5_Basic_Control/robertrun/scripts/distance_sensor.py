#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import rospy
import roslib
from sensor_msgs.msg import Range

def read_distance():
	ADC.setup() #set up ADC
	value = ADC.read("P9_39")#setup pin p9_39 as an ADC pin
	voltage = value * 3.2 #1.8V
	distance = (25.36 / (voltage+ .42)) / 100#convert from voltage to distance in meters
 	#distance = 0.01 DEBUG
 	return distance

if __name__ == '__main__':
	
	try:
		#Initialize node
		rospy.init_node('IR_sensor')
		pub = rospy.Publisher('range', Range, queue_size=10)
	except:
		pass
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		rangemsg = Range()#create a range msg
		rangemsg.range = read_distance() #get the range from the ADC
		try:
			pub.publish(rangemsg) #publish msg to joint_state 
		except rospy.ROSInterruptException:
			pass
    	rate.sleep()