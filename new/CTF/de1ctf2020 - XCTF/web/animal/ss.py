import socket,time
def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(("127.0.0.1",8800))
    sk.listen(5)
    #sk.setblocking(True)
    while True:
        conn,addr = sk.accept()
        print(addr)
        data = conn.recv(1024).decode()
        print(data)
        conn.sendall(bytes("HTTP/1.1 200 OK\r\n\r\n", "utf8"))
        if not data:
            print("close")
            conn.close()
    sk.close()
if __name__ == "__main__":
    main()
