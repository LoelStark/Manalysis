#Before insatlling anything, keep in mind. THis is for
#educational purposes only and I will not be held responsible for eany misuse

************************************************************************************************************

#if you dont have smbprotocol installed, run this command:
#pip install smbprotocol

#Subnet scanner
import socket
def sacn_subnet(base_ip="target ip"):
	live_hosts = []
	for i in range(1,255);
	try:
		socket.gethostaddr(ip)
		live_host.append(ip)
	except:
		continue
	return live_hosts
