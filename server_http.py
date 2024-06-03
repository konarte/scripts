import os
import socket
import time
 
def send_answer(conn, status="200 OK", typ="text/plain; charset=utf-8", data=""):
    data = data.encode("utf-8")
    conn.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")
    conn.send(data)
 
def get_on(conn, addr):
    data = b""
 
    while not b"\r\n" in data:
        tmp = conn.recv(1024)
        if not tmp:
            break
        else:
            data += tmp
 
    if not data:
        return
 
    udata = data.decode("utf-8")
    udata = udata.split("\r\n", 1)[0]
    method, addres, protocol = udata.split(" ", 2)
 
    if method != "GET" or addres != "/index.html":
        send_answer(conn, "404 Not Found", data="Не найдено")
        return
 
 
    file = open('D:/Temp/server/index.html')
    str1 = file.read()
    file.close()
    
 
    send_answer(conn, typ="text/html; charset=utf-8", data=str1)
 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)
 
 
try:
    while 1:
        conn, addr = s.accept()
        print("New connection from " + addr[0])
        try:
            get_on(conn, addr)
        except:
            send_answer(conn, "500 Internal Server Error", data="Ошибка")
        finally:
            conn.close()
finally: s.close()
