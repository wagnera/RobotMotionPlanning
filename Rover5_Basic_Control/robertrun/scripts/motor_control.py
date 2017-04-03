#!/usr/bin/python
#This script subscribes to the topics fr each motor command and using this input calculates 
#the required PWM, GPIO pins and settings to acheive the required motion 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from sensor_msgs.msg import JointState
import rospy
import roslib

class locomotion:
	def __init__(self): #sets up GPIO pins as outputs
		print "init DEBUG"
		
		GPIO.setup("P9_11", GPIO.OUT)
		print "init DEBUG pins 1"
		GPIO.setup("P9_12", GPIO.OUT)
		print "init DEBUG pins 2"
		GPIO.setup("P9_15", GPIO.OUT)
		print "init DEBUG pins 3"
		GPIO.setup("P9_13", GPIO.OUT)
		print "init DEBUG pins 4"
		GPIO.setup("P8_10", GPIO.OUT)
		print "init DEBUG pins 5"
		GPIO.setup("P8_12", GPIO.OUT)
		print "init DEBUG pins 6"
		GPIO.setup("P8_14", GPIO.OUT)
		print "init DEBUG pins 7"
		GPIO.setup("P8_16", GPIO.OUT)
		print "init DEBUG pins 8"
		PWM.start("P9_14", 0)
		PWM.start("P9_16", 0)
		PWM.start("P8_13", 0)
		PWM.start("P8_19", 0)
		print "PWM DEBUG start"

	def PinReset(self, motor): #had problem that if pins were not reset before changed beaglebone crashed
		print "pin reset DEBUG"
		if motor == 1:
			GPIO.output("P9_11", GPIO.LOW)#sets pins low
			GPIO.output("P9_12", GPIO.LOW)
		if motor == 2:
			GPIO.output("P9_13", GPIO.LOW)#sets pins low
			GPIO.output("P9_15", GPIO.LOW)
		if motor == 3:
			GPIO.output("P8_10", GPIO.LOW)#sets pins low
        	GPIO.output("P8_12", GPIO.LOW)
		if motor == 4:
			GPIO.output("P8_14", GPIO.LOW)#sets pins low
        	GPIO.output("P8_16", GPIO.LOW)
        
       
        

	#def Rmove(self, motor, speed):
	def Rmove(self, data):

		speed = 5*data.velocity[0]
		if speed > 100:
			speed = 100
		motor = data.name[0]

		print motor
		print speed

		
		if motor == "front_left_wheel":
			locomotion.PinReset(self, 1)#reset pins for that motor
			speedPWM = abs(int(speed))#convert input velocity to a pwm value
			PWM.set_duty_cycle("P9_14", speedPWM)#start pwm for that motor
			if speed > 0: #if the direction is forward
				GPIO.output("P9_12", GPIO.HIGH)
			elif speed < 0: #if the direction is backwards
				GPIO.output("P9_11", GPIO.HIGH)
			else:
				locomotion.PinReset(self,1) #reset the pins
		if motor == "rear_left_wheel":
			locomotion.PinReset(self,2)
			speedPWM = abs(int(speed))
			PWM.set_duty_cycle("P9_16", speedPWM)
			if speed > 0:
				GPIO.output("P9_15", GPIO.HIGH)
			elif speed < 0:
				GPIO.output("P9_13", GPIO.HIGH)
			else:
				locomotion.PinReset(self,2)
		if motor == "front_right_wheel":
			locomotion.PinReset(self,3)
			speedPWM = abs(int(speed))

			PWM.set_duty_cycle("P8_13", speedPWM)
			if speed > 0:
				GPIO.output("P8_10", GPIO.HIGH)
			elif speed < 0:
				GPIO.output("P8_12", GPIO.HIGH)
			else:
				locomotion.PinReset(self,3)
		if motor == "rear_right_wheel":
			locomotion.PinReset(self,4)
			speedPWM = abs(int(speed))
			PWM.set_duty_cycle("P8_19", speedPWM)
			if speed > 0:
				GPIO.output("P8_14", GPIO.HIGH)
			elif speed < 0:
				GPIO.output("P8_16", GPIO.HIGH)
			else:
				locomotion.PinReset(self,4)

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  Robert=locomotion()
  #Robert.__init__()
  try:
    #Initialize node
    rospy.init_node('motor_control')
       
    #create subscriber that subscribes to the /ticks topic and uses the callback function
    FLW_sub = rospy.Subscriber('/py_controller/front_left_wheel/cmd', JointState, Robert.Rmove)
    FRW_sub = rospy.Subscriber('/py_controller/front_right_wheel/cmd', JointState, Robert.Rmove)  
    BLW_sub = rospy.Subscriber('/py_controller/rear_left_wheel/cmd', JointState, Robert.Rmove)
    BRW_sub = rospy.Subscriber('/py_controller/rear_right_wheel/cmd', JointState, Robert.Rmove)

    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass



