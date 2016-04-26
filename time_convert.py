#!/usr/bin/evn python

# Imports time to use for the pauses or sleep in the code                         #
import sys
import time
from time import strftime


####################### CURRENT DATE AND TIME STAMP      ##########################
# This function provides a simple date and time stamp. Just call                  #
# door_timestamp(0). EXAMPLE: print(door_timestamp(0)- Sat, 27 Feb 2016 18:21:37  #

def door_timestamp(sec=0):
    if sec == 0:
        sec = time.time()
    return strftime("%a, %H:%M:%S - %d %b %Y", time.localtime(sec))


# print(door_timestamp(0))

#                                                                                 #
####################### CURRENT DATE AND TIME STAMP END    ########################

