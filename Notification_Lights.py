#!/usr/bin/python
import signal
import sys
import time

import RPi.GPIO as io

io.setmode(io.BCM)
io.setwarnings(False)


####################### SIGNAL HANDLER TO CATCH CTRL+C   ##########################
# Setup signal handler to catch ctrl+c detectGPIOn and exit cleanly               #
###################################################################################
def signal_handler(signal, frame):
    print(" ")
    print("Ctrl+C detected...")
    print(" ")
    io.cleanup()
    sys.exit(0)


# set signal handler                                                              #
signal.signal(signal.SIGINT, signal_handler)


#                                                                                 #
####################### SIGNAL HANDLER TO CATCH CTRL+C END ########################





ledPin = 17

# set up io output channel
io.setup(17, io.OUT)


#

# blinking function
def blink(pin):
    io.output(pin, io.HIGH)
    time.sleep(1)
    io.output(pin, io.LOW)
    time.sleep(1)
    return


def fblink():
    for i in range(0, 50):
        blink(17)

