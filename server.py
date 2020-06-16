#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import socket, random, os
from datetime import datetime

sock = socket.socket()
sock.bind(('', 1111))
sock.listen(1)
conn, addr = sock.accept()
conn.settimeout(60)

while True:
    response = 0
    message = input()
    conn.send(message.encode())

    while not response:
        try:
            response = conn.recv(1024)
            print(response.decode())
        except socket.timeout:
            print("Истекло время ожидания ответа")
            print("Переотправка")
            continue



