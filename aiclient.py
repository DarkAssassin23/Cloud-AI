#!/usr/bin/python3

import socket
import webbrowser
import ipaddress
import readline
from requests import get

# the host we are connecting to and the port
HOST = "127.0.0.1"
PORT = 4040

# Checks to see if the ip address is on a local network
def inLocalNetwork(ip):
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("192.168.0.0/16")):
		return True
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("192.0.0.0/24")):
		return True
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("198.18.0.0/15")):
		return True
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("172.16.0.0/12")):
		return True
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("100.64.0.0/10")):
		return True
	if(ipaddress.ip_address(ip) in ipaddress.ip_network("10.0.0.0/8")):
		return True
	if(ip=='127.0.0.1'):
		return True
	return False


# create our socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
response = -1
data = ""
try:
	while(not(data=="exit")):
		response = -1
		data = input(">> ")
		#if the user enters ipconfig or if config the response variable is set to 0
		#so modifications to the output can be made
		if(data=="ipconfig" or data=="ifconfig"):
			response = 0
		#if the user enters weather it prompts the user for a location
		elif(data=="weather"):
			city = input("Enter a city: ")
			data += city
		#if the user enters exit to quit the program it sets the response variable to 1
		#so it can break the connection once all the data has been sent and recieved
		elif(data=="exit"):
			response = 1
		#if the user enters a known website ending it will trigger the response veriable to 
		#2 so the client and send the user to the url given
		elif(".com" in data or ".net" in data or ".gov" in data or ".edu" in data or ".org" in data):
			web = data
			data = "web"
			response = 2
		#sets all of the data to lower case for easier managment
		data = data.lower().encode()
		sock.sendall(data)
		# read the response
		data = sock.recv(1024)

		# convert it to a string
		mesg = data.decode()

		#if the user wanted their ip address connects to 1.1.1.1 on port 80
		#and returns their local ip via the sockname. If the user doesn't have 
		#internet it checks to see if the server is running locally or on another
		#device on the network. If its running locally it will tell you you don't
		#have internet, otherwise it does the samething it did before but instead of
		#connecting to 1.1.1.1 it connects to the HOST. Finally it is connected to the
		#internet, it gets the global ip from either the server, if it isnt running locally
		#or via the site https://api.ipif.org 
		if(response==0):
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				s.connect(("1.1.1.1", 80))
				local_ip = s.getsockname()[0]
				s.close()
				print("Local IP: "+local_ip)
				if(inLocalNetwork(mesg)):
					global_ip = get('https://api.ipify.org').text
					print("Global IP: "+global_ip)
				else:
					print("Global IP: "+mesg)
			except:
				if(HOST=="127.0.0.1"):
					print("You are not connected to the internet and are running the server locally.")
					print("You have no internet access, and no IP address")
				else:
					s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					s.connect((HOST, 80))
					local_ip = s.getsockname()[0]
					s.close()
					print("Local IP: "+local_ip)
					print("Global IP: N/A")
					print("You are not connected to the internet and have no global IP")

		#if the user exits the program it gets the goodbye message from the server
		#then breaks
		elif(response==1):
			print(mesg)
			break
		#opens a web browser with the given url specifed by the user
		elif(response==2):
			webbrowser.open(web)
			print(mesg)
		#otherwise for basic resonces from the server it outputs them to the screen
		else:
			print(mesg)
	# and close the socket
	sock.close()

#Gracefull exit so server doesn't crash
except KeyboardInterrupt:
	data = "exit"
	sock.sendall(data.encode())
	data = sock.recv(1024)
	sock.close()
	print("\nGoodbye")
