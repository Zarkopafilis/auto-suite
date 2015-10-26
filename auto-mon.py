#!/usr/bin/env python
import subprocess

print "Automation tool to set interface to monitor mode by Zarkopafilis"
print ""
print "> ifconfig"
out = subprocess.check_output("ifconfig")
print out
print "> airmon-ng"
out = subprocess.check_output("airmon-ng")
print out
interface = raw_input("Enter interface > ")
x = raw_input("Set to monitor mode > ")
print "Shutting " + interface + "down..."
out = subprocess.check_output("ifconfig " + interface + " down" , shell=True)
print "Setting monitor mode..."
out = subprocess.check_output("iwconfig " + interface + " mode monitor", shell=True)
print "Bringing " + interface + "up"
out = subprocess.check_output("ifconfig " + interface + " up", shell=True)
print "All good"
