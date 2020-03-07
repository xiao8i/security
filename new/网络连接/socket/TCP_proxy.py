# -*- coding: utf-8 -*-
import socket, threading, sys, os
""" TCP代理实现  """


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
	#  监听client
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


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
	#  监听server
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connection((remote_host, remote_port))
	#  判断是否从server先收消息
	if receive_first:
		remote_buffer = receive_from(remote_socket)
		hexdump(remote_buffer)
		remote_buffer = response_handler(remote_buffer)

		if len(remote_buffer):
			client_socket.send(remote_buffer.encode())
			print("sending to local")
	flag_break = False

	while True:
		local_buffer = receive_from(client_socket)
		if len(local_buffer):
			hexdump(local_buffer)
			local_buffer = request_handler(local_buffer)
			remote_socket.send(local_buffer.encode())
			print("sending to remote")
			remote_buffer = receive_from(remote_socket)

			if len(remote_buffer):
				hexdump(remote_buffer)
				remote_buffer = response_handler(remote_buffer)
				client_socket.send(remote_buffer.encode())
				print("sending to localhost")
			else:
				flag_break = True
		else:  
			flag_break = True 

		if flag_break:
			client_socket.close()
			remote_socket.close()
			print("connection is closed")
		break


def hexdump(src, length = 16):
	#  十六进制及方便阅读格式
	result = []
	digits = 4 if isinstance(src, unicode) else 2

	for i in xrange(0, len(src), length):
		s = src[i: i + length]
		hexa = b''.join(["%0*X" % (digits, ord(x)) for x in s])
		text = b''.join([x if 0x20  <= ord(x) < 0x7F else b'.' for x in s])
		result.append(b"%04X  %-*s  %s" % (i, length * (digits + 1), hexa, text))
	print(b'\n'.join(result))


def receive_from(connection):
	#  接收数据
	buf = ""
	connection.settimeout(2000)
	try:
		while True:
			data = connection.recv(4096).decode()
			buf += data

			if len(data) < 4096:
				break
	except:
		pass
	return buf


def request_handler(buf):
	#  处理请求
	return buf


def response_handler(buf):
	#  处理响应
	return buf


def main():
	if len(sys.argv[1:]) != 5:
		print("Example：./TCP_proxy.py 127.0.0.1 8080 www.abc.com 80 True")
		sys.exit(0)

	local_host = sys.argv[1]
	local_port = int(sys.argv[2])
	remote_host = sys.argv[3]
	remote_port = int(sys.argv[4])
	receive_first = sys.argv[5]
	server_loop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__ == '__main__':
		main()	