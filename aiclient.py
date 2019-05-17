#!/usr/bin/python3

import socket
import webbrowser

# the host we are connecting to and the port
HOST = "35.185.5.147"
PORT = 4040

# create our socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
response = -1
data = ""
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

    #if the user wanted their ip address it uses the socket.gethostbyname and
    #socket.gethostname functions to get the local ip address
    #NOTE: depending on the machine this is running on it may give back a local ip
        #that is NOT your local network ip address. For example, while testing this
        #method on a windows machine it would return a virtual ethernet adapter in
        #this case it was 168.254.170.7 while the actual local ip was 192.168.1.6
        #On one of the linux computers this was tested on it returned the loopback
        #ip instead of the local ip, however on a different  linux computer it worked
        #fine and on the mac computer it was tested on it also worked fine.
        #However, to fix this problem on windows it is simply a problem with the binding 
		#order of your network adapters, so by changing the binding order of the network
        #adapters this will fix the problem. On linux, the solution is simple, in your
		#/etc/hosts/ file make sure your hostname is the local ip and not the loopback
		#adapter
    #Finally it gets the global ip from the and places it correctly there
	if(response==0):
		print("Local IP: "+socket.gethostbyname(socket.gethostname()))
		print("Global IP: "+mesg)
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
