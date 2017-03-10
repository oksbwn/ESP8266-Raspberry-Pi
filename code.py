import serial
import time

#Initialized Serial port.
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
def readlineCR(port): 
	rv = "" 
	#while 1:
	rv = port.read(5096) #Trying to read 5096 bytes max of data.
		#rv += ch
	return rv

#Checking connection by using AT.
isConnected=True;
while isConnected: #Looping till module is connected
	port.write("AT\r\n")
	returnedData=readlineCR(port)
	print(returnedData)
	if "OK" not in returnedData :
		print("Module not connected. Connect it and try Again.")
		time.sleep(60)
	else :
		print("Device connected.")
		isConnected=False
	
#Setting up ESP8266 module in STA mode.
port.write("AT+CWMODE=1\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Unable config Client.")
else :
	print("Confighured as STA.")

#Connecting to local network AP. Replace your SSID and password
port.write("AT+CWJAP=\"oksbwn-world\",\"omisoksbwn\"\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("WiFi not Connected.")
else :
	print("Connected to WiFi.")
	
#Configuring ESP8266 module to autoconnect to the connected Wi-Fi network.
port.write("AT+CWAUTOCONN=1\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Automatically Connection to the AP Disbaled.")
else :
	print("Automatically Connection to the AP enabled.")

#Printing out the IP of the module.
port.write("AT+CIFSR\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Failed to get IP")
else :
	print("Got IP")
	
#Starting a TCP connection to 192.168.0.1 with port 80.
port.write("AT+CIPSTART=\"TCP\",\"192.168.0.1\",80\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Initialization of TCP Connection Failed")
else :
	print("TCP Connection Initialized")

#Checking out the TCP connection status.
port.write("AT+CIPSTATUS\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Failed to get TCP status.")
else :
	pass

#Preparing to send 56 bytes of data through the connected TCP link. 
port.write("AT+CIPSEND=56\r\n")
returnedData=readlineCR(port)
print(returnedData)
if ">" not in returnedData :
	print("Unable to send")
else :
	print("Sending 18 bytes of Data.")	
	
#Setting up the payload for the GET call.
port.write("GET /ESP8266/index.php?NAME=myName /HTTP/1.0\r\n")
port.write("\r\n\r\n\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("WiFi not Connected.")
else :
	print("Connected to WiFi.")
	
#Closing the TCP connection
port.write("AT+CIPCLOSE\r\n")
returnedData=readlineCR(port)
print(returnedData)
if "OK" not in returnedData :
	print("Failed to close TCP Connection")
else :
	print("TCP Connection closed sucessfully.")
	
