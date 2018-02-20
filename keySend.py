import socket    # used for TCP/IP communication
import smtplib   # used to send email report
import time      # used to insert current date in email report
import sys

#if len(sys.argv) < 3:
#	print "Error: Need to Provide (rack, command, slot) as arguments"
#	sys.exit(0)

#key = sys.argv[2]


          
def keyPressAPI(rack, key, slot):	
	if rack == "A00":
		rack = "00-80-A3-A2-D9-13"
	elif rack == "A01":
		rack = "00-80-A3-A9-E3-68"	
	elif rack == "A02":
		rack = "00-80-A3-A9-E3-6A"
	elif rack == "A03":
		rack = "00-80-A3-A9-E3-7A"
	elif rack == "A04": 
		rack = "00-80-A3-A9-DA-67"
	elif rack == "A05":
		rack = "00-80-A3-A9-E3-79"
	elif rack == "A06":
		rack = "00-80-A3-A9-E3-78"
	elif rack == "A07":
		rack= "00-80-A3-9E-67-37"
	elif rack == "A08":
		rack = "00-80-A3-9D-86-D5"
	elif rack == "A09":
		rack = "00-80-A3-9D-86-CF"
	elif rack == "A10":
		rack = "00-80-A3-9E-67-27"
	elif rack == "A11": 
		rack = "00-80-A3-9E-67-34"
	elif rack == "A12":
		rack = "00-80-A3-9E-67-35"
	elif rack == "B04":
		rack = "00-20-4A-BD-C5-1D"
	elif rack == "B05":
		rack = "00-80-A3-9D-86-D2"
	elif rack == "B06":
		rack = "00-80-A3-9E-67-3B"
	elif rack == "B07":
		rack = "00-80-A3-9E-67-36"
	elif rack == "B08":
		rack = "00-80-A3-9E-67-32"
	elif rack == "B09":
		rack = "00-80-A3-9D-86-D6"
	elif rack == "B10":
		rack = "00-80-A3-9D-86-D3"
	elif rack == "B11":
		rack = "00-80-A3-9D-86-D1"
	elif rack == "B12":
		rack = "00-80-A3-9D-86-D0"
	else:
		print "Invalid Rack number inputted for first argument"
		sys.exit(0)


#Prepare 3-byte control message for transmission
        TCP_IP = '10.23.223.36'
        TCP_PORT = 40000
        BUFFER_SIZE = 1024
        MESSAGE = 'MAC="' + rack + '" dataset="RC71" signal="' + key + '" output="' + slot + '" \n'
#Open socket, send message, close scoket
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p.connect((TCP_IP, TCP_PORT))
        p.send(MESSAGE)
        data = p.recv(BUFFER_SIZE)
        p.close()
        print "Return Data: " + str(data) + key
#keyPressAPI(rack, key, "1-16")




def tune(channel, rack, slot):
	
	for i in channel:
		print i
		keyPressAPI(rack, i, slot)
		time.sleep(1)

	return "Function to tune to channel" 
