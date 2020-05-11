import socket,time,threading

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("",80))
    server.listen(5)
    server.setblocking(False)
    client = list()
    while True:
        try:
            conn,addr = server.accept()
        except Exception as e:
            pass
        else:
            conn.setblocking(False)
            client.append(conn)
        for l in client:
            try:
                data = conn.recv(1024).decode()
            except Exception as e:
                pass
            else:
                if data:
                    print(data)
                    conn.send("HTTP/1.1 200 OK\r\nConnection: keep-alive\r\n\r\nx".encode("utf-8"))
                else:
                    conn.close()
                    client.remove(conn)
    server.close()
        
if __name__ == "__main__":
    main()
