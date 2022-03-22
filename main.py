import subprocess
from time import sleep
import re
INTERFACE = 'wlan0'

output = subprocess.check_output("sudo arp-scan --interface=" + INTERFACE + " --localnet" + " | awk '/.*:.*:.*:.*:.*:.*/{print $2}'", shell=True)
#print(output)
f = open("output.txt", "a")
f.write(output)
resultList = output.split("\n")
print "\n",resultList, len(resultList)
f.close()
