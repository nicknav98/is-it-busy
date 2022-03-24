import subprocess
from time import sleep
import paho.mqtt.publish as publish
import re
INTERFACE = 'wlan0'

MQTT_HOST = "172.27.227.5"
MQTT_PORT = "1883"



def func():
	output = subprocess.check_output("sudo arp-scan --interface=" + INTERFACE + " --localnet" + " | awk '/.*:.*:.*:.*:.*:.*/{print $2}'", shell=True)
	print(output)
	f = open("output.txt", "a")
	f.write(output)
	resultList = output.split("\n")
	print "\n",resultList[1:], len(resultList)-1
	f.close()
	pplnumber = str(len(resultList) - 1)


	publish.single("home/mac", pplnumber + " People Are Currently in Embedded Lab", hostname=MQTT_HOST, port=MQTT_PORT)

def keepRunning():
	func()
	sleep(30)
	keepRunning()

keepRunning()
