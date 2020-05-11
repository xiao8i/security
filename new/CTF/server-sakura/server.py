import socket, threading, time,multiprocessing
# 建立一个服务端
def tcplink(conn, addr):
    print(conn)
    while True:
        try:
            data = conn.recv(4096).decode()
            print(data)
            #conn.sendall(bytes("HTTP/1.1 200 OK\r\n\r\n", "utf8"))
            if not data:
                print("\r\nclose\r\n")
                conn.close()
                break
        except:
            pass

def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(("127.0.0.1",8800))
    sk.listen(256)
    #sk.setblocking(True)
    while True:
        conn,addr = sk.accept()
        t = threading.Thread(target = tcplink,args = (conn, addr))
        #t = multiprocessing.Process(target = tcplink,args = (conn, addr))
        t.start()
        #t.join()
    sk.close()
if __name__ == "__main__":
    main()
