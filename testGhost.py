# -*- coding: utf-8 -*-
import sys
reload(sys)
import datetime
import time
sys.setdefaultencoding("utf-8")

from ghost import Ghost
ghost = Ghost(wait_timeout=20)

url = "http://weixin.sogou.com/gzh?openid=oIWsFt8JDv7xubXz5E3U41T0eFbk"
page, resources = ghost.open(url)
result, resources = ghost.wait_for_selector("#wxmore a")

from bs4 import BeautifulSoup
c = 0
while True:
    if c >= 30:
        break

    soup = BeautifulSoup(ghost.content)

    for wx in soup.find_all("h4"):
        print wx

    page, resources = ghost.evaluate(
        """
        var div1 = document.getElementById("wxbox");
        div1.innerHTML = '';
        """)
    ghost.click("#wxmore a")
    result, resources = ghost.wait_for_selector(".wx-rb3")

    c = c + 1
    pass
