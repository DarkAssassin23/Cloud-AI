#!/usr/bin/python3
import socket
import datetime as dt
import urllib.request
import urllib.parse
import random
import calendar
from datetime import datetime
# host (internal) IP address and port
HOST = "10.142.0.2"
PORT = 4040

# create our socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow us to reuse an address for restarts
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# set the socket host and port number up
sock.bind((HOST, PORT))
connected = False
name = ""
while True:
        if(not connected):
                # listen for any clients connecting
                sock.listen()
                name = ""
                # wait for a client to connect to us
                # accept a connection which has come through
                conn, addr = sock.accept()
                print("Connection from:", addr)

        # read some bytes from the client
        data = conn.recv(1024)

        # decode it into a string
        string = data.decode()
        #parses the address so it returns the global ip of the user
        if(string=="ifconfig" or string=="ipconfig"):
                data = str(addr)
                data = data.split(" ")
                data = data[0]
                data = str(data[2:-2])
                connected = True
        #makes a joke refrence from the Star Wars prequals
        elif(string=="hello there"):
                data = "General Kenobi\nSorry I had to use the Star Wars refrence"
                connected = True
        #returns the time back to the user in Hour:Minut:Second format
        elif(string=="time"):
                data = "The time is: "+datetime.now().strftime('%H:%M:%S')
                connected = True
        #returns the date to the user in MM?DD?YYYY format
        elif(string=="date"):
                data = "The date is: "+datetime.now().strftime('%m/%d/%Y')
                connected = True
        #returns the calendar of the current month
        elif(string=="calendar"):
                data = "Here is the Calendar for the month: \n"+calendar.month(int(datetime.now().strftime('%Y')),int(datetime.now().strftime('%m')))
                connected = True
        #returns the weather of the given locaiton
        elif(string[:7]=="weather"):
                location = string[7:]
                url = "http://wttr.in/"+location+"?format=3"
                data = urllib.request.urlopen(url)
                data = data.read().decode("utf-8")
                connected = True
        #randomly generates a response for the user
        elif(string=="how are you"):
                num = random.randint(0,4)
                if(num==0):
                        data = "I am doing good"
                elif(num==1):
                        data = "I'm Fantastic!"
                elif(num==2):
                        data = "I'm bored"
                else:
                        data = "Tired"
                connected = True
        #based on who you say you are that gets set as the name variable
        #so the AI knows who you are and can address you while you're 
        #connected
        elif(string[:5]=="i am "):
                name = string[5:]
                data = "Hello "+name
                connected = True
                
        #if the user has set their name the AI respondes with their name
        #otherwise it tells the user they don't know an dhow they can set
        #their name
        elif(string=="whoami" or string=="who am i"):
                connected = True
                if(name==""):
                        data = "You haven't told me your name. Tell me by typing \"I am\" followed by your name"
                else:
                        data = "You\'re name is "+name
        #The AI gives information about itself
        elif(string=="who are you"):
                data = "I am Sarah, the AI, and I live on a virtual machine in the google cloud on my creator, Will Jones's, server for CPSC 414"
        #if the user wants to add two numbers the server takes those two
        #adds them togeather then formats the number and sends it to the
        #user
        elif("+" in string):
                string = string.replace(" ","")
                number = string[:(string.index("+"))]
                number2 = string[(string.index("+")+1):]
                answer = float(number)+float(number2)
                if(answer%1==0):
                        answer = int(answer)
                data = number+" + "+number2+" = "+str(answer)
                connected = True
        #if the user wants to subtract two numbers the server takes those two
        #subtracts them then formats the number and sends it to the
        #user
        elif("-" in string):
                string = string.replace(" ","")
                number = string[:(string.index("-"))]
                number2 = string[(string.index("-")+1):]
                answer = float(number)-float(number2)
                if(answer%1==0):
                        answer = int(answer)
                data = number+" - "+number2+" = "+str(answer)
                connected = True
        #if the user wants to multiply two numbers the server takes those two
        #multiplies them then formats the number and sends it to the
        #user
        elif("*" in string):
                string = string.replace(" ","")
                number = string[:(string.index("*"))]
                number2 = string[(string.index("*")+1):]
                answer = float(number)*float(number2)
                if(answer%1==0):
                        answer = int(answer)
                data = number+" * "+number2+" = "+str(answer)
                connected = True        
        #if the user wants to divide two numbers the server takes those two
        #divdes them then formats the number and sends it to the
        #user
        elif("/" in string):
                string = string.replace(" ","")
                number = string[:(string.index("/"))]
                number2 = string[(string.index("/")+1):]
                answer = float(number)/float(number2)
                if(answer%1==0):
                        answer = int(answer)
                data = number+" / "+number2+" = "+str(answer)
                connected = True
        #if the user wants to modulo two numbers the server takes those two
        #modulos them then formats the number and sends it to the
        #user
        elif("%" in string):
                string = string.replace(" ","")
                number = string[:(string.index("%"))]
                number2 = string[(string.index("%")+1):]
                answer = float(number)%float(number2)
                if(answer%1==0):
                        answer = int(answer)
                data = number+" % "+number2+" = "+str(answer)
                connected = True
        #this comand takes a decimal number and converts it to 
        #a binary number
        elif("to binary" in string):
                if("t"==string[:(len(string)-(len(string)-1))]):
                        data = "No number given"
                else:
                        string = string.replace(" ","")
                        number = string[:string.index("t")]
                        binary = bin(int(number))
                        data = number+" --> "+str(binary)
                connected = True
        #this comand takes a decimal number and converts it to
        #hexadecimal
        elif("to hex" in string):
                if("t"==string[:(len(string)-(len(string)-1))]):
                        data = "No number given"
                else:
                        string = string.replace(" ","")
                        number = string[:string.index("t")]
                        hexNum = hex(int(number))
                        data = number+" --> "+str(hexNum)
                connected = True
        
        elif(string=="web"):
                data = "I'll take you there"
                connected = True                                 
        #if the user types exit to leave the AI says good by to them
        #and sets the connected variable to flase to disconect the user
        #and wait for an new user to connect    
        elif(string=="exit"):
                data = "Goodbye"
                connected = False
        #if the user enters an un recognized comand the AI tells them
        #the comand is not recognized
        else:
                data = "Invalid command"
                connected = True
        data.encode()
        # send it back
        conn.sendall(data.encode())
        #if the user has disconnected via the exit command it closes the 
        #connection
        if(not connected):
                conn.close()

# done with listening on our socket to
sock.close()
