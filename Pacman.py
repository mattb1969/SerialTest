#!/usr/bin/env python3


import serial, time, sys


s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"

all_off = ("$$$ALL,OFF\r").encode('utf-8')
open_mouth = ("$$$F000000000000000000000111000011111110011111110111111111111101111111101111011000110011000110000000000000000000000000000000000000\r").encode('utf-8')
closed_mouth = ("$$$F000000000000000000000111000011111110011111110111111111111111111111111111011111110011111110000111000000000000000000000000000000\r").encode('utf-8')
try:
    s.open()
except (serial.SerialException, e):
    sys.stderr.write("could not open port %r: %s\n" % (s.port, e))
    sys.exit(1)

s.write(all_off)
time.sleep(0.5)
while True:
    s.write(open_mouth)
    time.sleep(0.5)
    s.write(closed_mouth)
    time.sleep(0.5)

