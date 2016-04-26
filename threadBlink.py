#!/usr/bin/evn python

import threading
import sys
import time
import DoorAlarm
from time_convert import door_timestamp

def tledBlink():
    # Setting up the multiprocessing threading
    # print('Starting:', multiprocessing.current_process().name, door_timestamp(0))
    DoorAlarm.fblink()
    return
    # print('Exiting :', multiprocessing.current_process().name, door_timestamp(0))

def teal():
    # Setting up the multiprocessing threading
    # print('Starting:', multiprocessing.current_process().name, door_timestamp(0))
    emailParser.emailalert()
    return
    # print('Exiting :', multiprocessing.current_process().name, door_timestamp(0))

def main1():
    tled = Timer(0.5, tledBlink)
    temal = Timer(0.5, teal)

    tled.start()
    temal.start()

    return

    #
    # tl = multiprocessing.Process( name='tledBlink', target=tledBlink )
    # tl.daemon = True
    #
    # # Starting multiprocessing
    # te.start( )
    # tl.start( )
    #
    # # Joining the processes to end at the same time
    # te.join( )
    # tl.join( )

if __name__ == '__main__':
    main1()