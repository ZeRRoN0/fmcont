#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanize
#color
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
br = mechanize.Browser()
br.set_handle_robots(False)
oku = br.open("https://mbasic.facebook.com/login/identify/")
br._factory.is_html = True
def logo():
    print green+"*******************************"
    print green+"*"+red+"   Facebook Mail Sorgulama   "+green+"*"
    print green+"*"+red+"     coding:'ZeRRoN-HACK'    "+green+"*"
    print green+"*******************************"

logo()
scan_User = raw_input(yellow+"Aranacak Mail Adresi Girin:"+green)
br.select_form(nr=0)
br.method="POST"
br["email"]=scan_User
git = br.submit().read()
bul = """<div class="h">"""
bul1 = """id="login_identify_search_error_msg">"""

if bul1 in git:
    print green+"[+]Bu Eposta Adresi Kullanılmamış"
elif bul in git:
    pass
else:
    print red+"[x]Bu Eposta Adresi Kullanılmış"

