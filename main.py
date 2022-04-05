import argparse
import subprocess
from time import sleep
import paho.mqtt.publish as publish
import re
INTERFACE = 'wlan0'

#MQTT_HOST = ""
#MQTT_PORT = ""

# parser arguments
parser = argparse.ArgumentParser(description='is-it-busy')
parser.add_argument('--host', default = 0)
parser.add_argument('--port', default = 0)
parser.add_argument('--sub', default = "home/mac")
parser.add_argument('--sleeptime', type=int, default = 30)
parser.add_argument('--roomname', default="Room")
args = parser.parse_args()
# drop on invalid input
if args.host==0 or args.port==0:
        print("No arguments were set, script failed to initialize.")
else:
        print(args.host, args.port, args.sub, args.sleeptime, args.roomname)


        def func():
                output = subprocess.check_output("sudo arp-scan --interface=" + INTERFACE + " --localnet" + " | awk '/.*:.*:.*:.*:.*:.*/{print $2}'", shell=True)
                print(output)
                f = open("output.txt", "a")
                f.write(output)
                resultList = output.split("\n")
                print "\n",resultList[1:], len(resultList)-1
                f.close()
                pplnumber = str(len(resultList) - 1)


                publish.single(args.sub, pplnumber + " People Are Currently in " + args.roomname, hostname=args.host, port=args.port)

        def keepRunning():
                func()
                sleep(args.sleeptime)
                keepRunning()
        func()
        keepRunning()


