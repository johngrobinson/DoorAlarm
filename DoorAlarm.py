#!/usr/bin/env python2.7

# Declaring the modules I will be using for this project.
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import RPi.GPIO as GPIO

from time_convert import door_timestamp

# This code sets the Pi to initiate the GPGPIO pin so we can use them
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Sets the variable door_pin to GPGPIO 26
door_pin = 26

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
var = 1


'''
####################### SIGNAL HANDLER TO CATCH CTRL+C   ##########################
#       Setup signal handler to catch ctrl+c detectGPGPIOn and exit cleanly         #
###################################################################################
'''


def signal_handler(signal, frame):
	print("Ctrl+C detected...")
	GPIO.cleanup()
	sys.exit(0)


####################### EMAIL CREATGPION SECTGPION START ##########################
# This code is used to email out a notificatGPIOn if the magnetic door sensor has #
# been triggered.                                                                 #
# Begin mail setup, this code is written for GMAIL but you could easily re-write  #
# the current code by changing the GMAIL setup properties with Hotmail or what    #
# ever smtp mail service.                                                         #
###################################################################################

def emailalert():
	print("Email being sent!")
	# GMAIL user setup #
	gmail_sender = 'johngrobinson@gmail.com'
	gmail_passwd = 'Monkeybutt2'
	you = "jrotton@hotmail.com"
	# , Sjcarrillo2@gmail.com
	# GMAIL SMTP Server connect
	smtp_host = 'smtp.gmail.com'
	smtp_port = 587
	server = smtplib.SMTP(smtp_host, smtp_port)
	server.ehlo()
	server.starttls()
	server.login(gmail_sender, gmail_passwd)

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'TEST TEST - Do you know where you daughter is? - TEST TEST'
	msg['From'] = gmail_sender
	msg['To'] = you

	b1 = '<html><head></head><body><p><br><br>Do you know where you daughter is?<br><br>Your front door was opened at: '
	b2 = door_timestamp(0)
	b3 = ' </p><BR><BR><BR>The Alarm!<br><br>John Robinson</body></html>'

	# Create the body of the message (a plain-text and an HTML versGPIOn).
	# text = (
	# "Do you know where you daughter is? \n Your front door was opened at: ", door_timestamp(0), "\n\n The Alarm")
	html = (b1 + b2 + b3)

	# Record the MIME types of both parts - text/plain and text/html.
	# part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	# msg.attach(part1)
	msg.attach(part2)
	# Send the message via gmail SMTP server.
	# sendmail functGPIOn takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	server.sendmail(gmail_sender, [you], msg.as_string())
	server.quit()
	print('\nEmail has been sent!\n')
	return True

# Define a threaded callback function to run in another thread when events are detected
def my_callback():
	if var == 1:
		time.sleep(1.5)  # confirm the movement by waiting 1.5 sec
		if GPIO.wait_for_edge(26, GPIO.FALLING):  # and check again the input
			print("Door Open! ", GPIO.event_detected(26))
			emailalert()
			# removes the event detection on PIN 26
			GPIO.remove_event_detect(26)
			# wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
			GPIO.wait_for_edge(26, GPIO.RISING)
			print("Door Closed! ")
			time.sleep(5)
		else:
			time.sleep(15)
			pass

while True:

	print('Output is cleared - ', GPIO.input(26))
	GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback, bouncetime=300)






