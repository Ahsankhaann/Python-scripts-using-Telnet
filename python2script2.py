import getpass
import sys
import telnetlib

HOST = "192.168.122.71"
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name python_vlan_2\n")
tn.write("vlan 3\n")  
tn.write("name python_vlan_3\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
