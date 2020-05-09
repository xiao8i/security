import socket,time,threading

def tcplink(conn, addr):
    print(addr)
    while True:
        print(conn.recv(1024).decode())
        header = "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\n\r\n"
        body = "x"
        response = header + body
        conn.send(response.encode("utf-8"))
        print("___")

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("",80))
    server.listen(5)
    while True:
        conn,addr = server.accept()
        t = threading.Thread(target = tcplink,args = (conn, addr))
        t.start()
    server.close()
        
if __name__ == "__main__":
    main()
