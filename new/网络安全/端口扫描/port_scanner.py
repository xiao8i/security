import sys, os, nmap


"""nmap端口扫描"""
nm = nmap.PortScanner()
nm.scan("127.0.0.1", "1-1024")       
for host in nm.all_hosts(): #  扫描主机列表
	print("-"*100)
	print("host: {0}({1})".format(host, nm[host].hostname())) #  主机IP与名称
	print("state: {0}".format(nm[host].state())) #  主机状态
	for proto in nm[host].all_protocols():
		print("protocal {0}".format(proto)) #  输出主机协议
		lport = list(nm[host][proto].keys()) #  开放端口  
		lport.sort()
		for port in lport:
			print("port: {0}\tstate:{1}".format(port, nm[host][proto][port]))

