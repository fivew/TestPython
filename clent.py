# -*- coding: utf-8 -*-

import socket

from socket import *

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("www.baidu.com", 80))
print "connect from ", c.getsockname()
print "connect to", c.getpeername()

c.close()
