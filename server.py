#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import socket, random, os
import time
from datetime import datetime
from collections import deque
import threading

def thread_fun(messages):
    while True:
        message = input()
        messages.append(message)

if __name__ == "__main__":
    sock = socket.socket()
    sock.bind(('', 1111))
    sock.listen(1)
    conn, addr = sock.accept()
    conn.settimeout(60)

    messages = deque()

    x = threading.Thread(target=thread_fun, args=(messages,))
    x.start()

    while True:
        if len(messages) > 0:
            response = 0
            message = messages.popleft()
            conn.send(message.encode())
            while not response:
                try:
                    response = conn.recv(1024)
                    print(response.decode())
                except socket.timeout:
                    print("Истекло время ожидания ответа")
                    print("Переотправка")
                    continue