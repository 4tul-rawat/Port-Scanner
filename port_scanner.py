#Logic Flow

#Check if the number of arguments are sufficient (sys.argv-length)
#Store the target IP value using sys.argv[1]
#Open a for loop for all the values between 1-65535
#Create a new socket object i.e. s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Establish a connection i.e. s.connect_ex((target,port))
#Close the connection
#Define some exceptions that can occur during the process.

import pyfiglet
import socket
import sys

from datetime import datetime

#Adding a banner
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

# Defining a target 
if len(sys.argv) == 2:
	# Translate the hostname into IPv4
	target = socket.gethostbyname(sys.argv[1])
else: 
	print("The number of arguments provided with the script are not sufficient")
	sys.exit()

#Adding a banner 

print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)
print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)
print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)
print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)
print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)
print("*" * 50)
print("Hello world")
print("Port Scanning Target:" + target)
print("*" * 50)
print("*" * 10)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))

		s.close()

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))

		s.close()
try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))

		s.close()

except KeyboardInterrupt:
	print("\n####Exiting Program####")
	sys.exit()

except socket.gaierror:
	print("\n Host name couldn't be resolved")

except socket.error:
	print("\n Server is not responding")
