# -*- coding:utf-8 -*-

import socket

host = ''
port = 1345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

s.listen(9)

while True:
    clientfd, clientAddr = s.accept()
    clientFile = clientfd.makefile('rw', 0)
    clientFile.write("user form " + str(clientAddr) + "\n")
    clientFile.write("Enter:")
    line = clientFile.readline().strip()
    clientFile.write("you enter the string %s\n" % (line))
    clientFile.close()
    clientfd.close()
