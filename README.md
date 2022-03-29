# Is It Busy ?

  
This project is done with association of Turku University of Applied Sciences. 

This package allows end-users to run a sniffing node in their WIFI-networks to estimate how many people are connected to their network based on connected devices. This script counts unique mac addresses connected to the network and publishes a MQTT message with the result. We realize router firmware has tools already in place to see the amount of devices connected, but this allows a more accurate count to be done based on location, and information can easily be displayed to users on the network. An example would be running this proccess on a library network, and a user can see on their main page how 'busy' the library is. 



## Contributors

- [@Nicholas Navarro](https://www.github.com/nicknav98) - Student at Turku AMK
- [@Michalis Iona](https://www.github.com/MikeByBike) - Student at Turku AMK with a degree at Beng Information and Communication Technology
- [@Georgi Georgiev](https://www.github.com/GeorgiRG) - Student at Turku AMK

## Pre-requisites 

- Linux Distro that Supports ARP Commands
- Dual-WIFI or Ethernet + WIFI Connection Supported. 
- Docker Service Installed and Enabled
- Python 2.7 Virtual Environment


-------------------------------------------
This project was built using a Raspberry Pi 3+ 4GB with 32-bit Kali Linux Installed. 

## How to Install and Run Script

First install python2.7 and Virtual-Environment on your remote node (e.g. Raspberry Pi 3)

If you are running on a Debian-based distro, use the following:

    sudo apt-get install virtualenv
    sudo apt-get install python2.7

Secondly, get your docker.service started on your device that will be running the mosquitto-mqtt container. This needs to be separate to your raspberry pi, but connected on a network that they both share. For example, A Laptop and Raspberry Pi connected through ethernet on a shared router or network switch. 

To start docker, enable using: 

    sudo systemctl docker.service start

Clone this repository into a directory of your choosing, on both your node and server host

    sudo git clone https......

## FOR YOUR NODE, DO THE FOLLOWING: 

Create a virtual enviroment folder in the same directory using this command:

    virtualenv --python=2.7 venv

Then activate this virtual environment by doing the following:

    source venv/bin/activate

 Now install requirements:

    pip install -r requirements.txt

Now your node is ready to be launched. Before deploying this into your target network. First make sure your node is connected to the target wifi, and your device  running the mqtt container has the ability to open ports and is visible on the network. A quick way to confirm to to run: `ifconfig -a` on a linux, take note of your public ip address, and run the following command on your node: 

    sudo arp-scan [DEVICE IP ADDRESS]

You should get a response like the following: 
- Image

## FOR YOUR DEVICE RUNNING THE CONTAINER DO THE FOLLOWING: 

Check that docker is running by running: 

    sudo systemctl status docker.service

Now since docker is running, run this command in the directory of the repository: 

    docker-compose up -d 

The default port is 1883 and the script is written so ports and ip's are configurable. You will need to change the IP ADDRESS variable to your devices IP to ensure published messages are being sent to your mqtt container. 

## Checking you are receiving published messages

Using MQTT X: https://mqttx.app/ , you can subscribe to the board using hostname: localhost, and port: 1883. The script uses a default path of `home/mac`. Again this is configurable in the script, and each node can have different boards to publish to, for example: `mainlibrary/area1`. If you would like to run MQTT.X on a different device altogether, be sure you use the docker container's device IP. 



You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Running Examples
- Gifs
- Images

