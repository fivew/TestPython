# -*- coding: utf-8 -*-

import urllib
import sys

f = urllib.urlopen("https://www.google.com.hk/?gws_rd=cr,ssl")

while True:
    buf = f.read(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
