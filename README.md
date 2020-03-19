# Cloud AI
About
--------
This is a semi-smart, cloud-based AI system designed to make your life easier.
This contains both the client and the server scripts.

--------------------
Commands
-------
	
	calendar		This command will return the calendar for the current month

	date			This command will return the current date to the user in 
					MM/DD/YYYY format
	
	exit 			This command closes your connection to the server

	hello there 		This command will give you a Star Wars prequals reference

	how are you		This command will result in the AI telling you how they are
	 				feeling at that moment. There are multiple feelings it can 
					feel, so feel free to see if you can find them all

	i am 			This command lets the AI know who you are and will address 
					you by that name (when applicable) though out the course of 
					your connection to the server

	ipconfig		This commands will give you your local IP as well as your
				 	global IP. NOTE: depending on the machine this is running on 
					it may give back a local ip that is NOT your local network ip 
					address. For information on how to fix this, see the Local IP
					Configuration section 

	ipconfig		This commands will give you your local IP as well as your
				 	global IP. NOTE: depending on the machine this is running on 
					it may give back a local ip that is NOT your local network ip 
					address. For information on how to fix this, see the Local IP
					Configuration section  
	
	time			This command will return the current time to the user in 
					military time

	to binary		This command takes a base 10 number followed by 'to binary' 
					and returns to you the binary representation of that base 10 
					number

	to hex			This command takes a base 10 number followed by 'to hex' and 
					returns to you the hexadecimal representation of that base 10 
					number

	weather			This command will then prompt you for the city you want the 
					weather for. Then it will return the weather for that city

	who are you		This command will return the AI telling you who it is and a 
					little bit about itself

	whoami			This command will result in the AI saying who you are. If you
		 			have not given the AI your name it will tell you how you can 
					tell it your name, otherwise it says your name

	who am i		This command will result in the AI saying who you are. If you
		 			have not given the AI your name it will tell you how you can 
					tell it your name, otherwise it says your name
Other Features
------
- ### Simple math
	You can enter math problems such as 4+6, 8/2, 92-56, 7*23, 10%4 etc.	
	the AI will solve these problems and return the answer to you (it also works with decimal numbers) 

- ### Web browsing
	Enter your favorite websites (ending in .com, .edu, .gov, .net, or .org) and   the AI will open up a web browser with that website	
	
---------
Local IP Configuration
-----
Depending on the machine this is running on it may give back a local ip
that is NOT your local network ip address. 

For example, while testing this
method on a Windows machine it would return a virtual ethernet adapter, in
this case it was 168.254.170.7, while the actual local ip was 192.168.1.6.

On one of the Linux computers this was tested on it returned the Loopback
IP instead of the Local IP, however on a different linux computer it worked
fine. 

On the macOS computer it was tested on it also worked fine.

However, to fix this problem on Windows, it is simply a problem with the binding 
order of your network adapters; so, by changing the binding order of the network
adapters this will fix the problem. On linux, the solution is simple, in your
/etc/hosts/ file make sure your hostname is the local ip and not the loopback
adapter
	
