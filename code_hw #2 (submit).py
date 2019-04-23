from microbit import *
# import machine and time modules
import machine
import time
# import pin module
from machine import Pin
# specify triger pin is connected to pin0 on microbit, and provides output
trigger_pin = Pin(0, machine.Pin.OUT, pull=None)
# sleep for 0.002ms
machine.lightsleep([0.002])
# specify echo pin is connected to pin1 on microbit, and provides output
echo_pin = Pin(1, machine.Pin.IN, pull=None)
# sleep for 0.01ms
machine.lightsleep([0.01])
# set variables for soundwave travel start and stop time
start = time.time()
stop = time.time()
while echo_pin == 0:
    # starting the time when sending out the signal
        start = time.time()
while trigger_pin == 1:
    # Stopping the time when the signal comes back
        stop = time.time()
# time of sound traveled one way between trigger and echo
time_difference = (stop-start) / 2
# multiply by speed of sound to get distance
distance = time_difference * 1129000
# diaplay distance
display.scroll(str(distance))