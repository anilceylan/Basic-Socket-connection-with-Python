import socket

ip_address = input("Enter the IP address: ")
scan_startPort = int(input("Enter the start port number for scanning: "))
scan_stopPort = int(input("Enter the stop port number for scanning: "))

#ip_address = "10.0.2.254" --> your target IP address


for port in range(scan_startPort,scan_stopPort):
	try:
		Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Socket.connect((ip_address,port))
		info = str(Socket.recv(1024))
		print ("Port Number :",str(port))
		print ("Info :", info)
		Socket.close()
	except:
		pass
