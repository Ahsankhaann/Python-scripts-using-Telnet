import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP=IP.strip()
    print ('Configuring switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'conf t\n')

    for n in range (2,11):
        tn.write(b'vlan ' + str(n).encode('ascii') + b'\n')
        tn.write(b'name Python_vlan_' + str(n).encode('ascii') + b'\n')

    tn.write(b'end\n')
    tn.write(b'wr\n')
    tn.write(b'exit\n')

    print (tn.read_all().decode('ascii'))
    
    
    #This script is assuming that your user credential are consistent across every device in the network and they have a prvilege level of 15.
    #Therefore, no enable password is needed
  
