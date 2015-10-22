from enum import *
import rospy
from robotino_leds.srv import *

def ligandoLeds(colors, terminou):
	if terminou:
		sinalize = rospy.ServiceProxy('sinalize', Sinalize)
		resp = sinalize(0, colors, 0, 1)
	sinalize = rospy.ServiceProxy('sinalize', Sinalize)
	if colors[0] == colors[1]:
		resp = sinalize(1, colors, 2, 1)
	else:
		resp = sinalize(1, colors, 1, 1)	 
	rospy.logwarn('Liguei led %s', colors)

def desligandoLeds():
	stop_sinalization = rospy.ServiceProxy('stop_sinalization', Trigger)
	resp = stop_sinalization()
	rospy.logwarn('Desliguei led')
