# -*- coding: utf-8 -*-
import socket, threading, sys
 #  TCP代理实现


 #  监听client
def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.bind(local_host, local_port)
	except:
		print("Failed to listen on %s:%d" %(local_host, local_port))
		sys.exit(0)
	else:
		print("Listening on %s:%d" %(local_host, local_port))
	server.listen(5)
	while True:
		client_socket, addr = server.accept()
		print("Received connection from %s:%d" %addr)
		proxy_thread = threading.Thread(target = proxy_handler, args = (client_socket, remote_host, remote_port, receive_first))
		proxy_handler.start()


 #  监听server
def proxy_handler(client_socket, remote_host, remote_port, receive_first):
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connection((remote_host, remote_port))
	#  判断是否从server先收消息
	if receive_first:
		pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                