from scapy.all import *


"""尝试将scapy与nfqueue模块结合起来。nfqueue模块允许您修改（使用scapy）满足特定的iptables规则的数据包"""
def intercept(pkt):

   if pkt.haslayer(Raw):
      http_content = pkt.getlayer(Raw).load
      http_content = http_content.replace("Accept-Encoding: gzip, deflate", "Accept-Encoding: identity")
      pkt[Raw].load = http_content         
      print pkt.show()
      send(pkt)


def main():
   sniff(iface='lo', filter='tcp port 80', prn=intercept)

if __name__ == '__main__':
   main() 