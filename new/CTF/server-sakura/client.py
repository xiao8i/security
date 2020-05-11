import socket
#socket通信客户端
def client():
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect(('127.0.0.1',8800))
    while True:
        m = input(":").encode()
        mysocket.send(m)
        try:
            data=mysocket.recv(1024).decode()
        except:
            pass

        if data:
           print(data)
        #else:
            #break
    mysocket.close()
client()
