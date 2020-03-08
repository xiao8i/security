# -*- coding: utf-8 -*-
import socket


#  创建client TCP
host = "www.abc.com"
port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("发送的数据")
response = client.recv(4096)
print(response)
client.close()


#  创建server TCP
ip = "0.0.0.0"
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)
while True:
	client，addr = server.accept()
	print("connection from:%s" %str(addr))
	request = client.recv(1024)
	print(request)
	client.send("Copy that!")
	client.close()