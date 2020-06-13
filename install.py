#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from time import sleep
######################################################################################################################################
path = os.path.abspath("./")
path_reqairement = path + "/" + "reqairement.txt"
# обновляем пакеты
os.system("sudo apt-get update")
# Устанавливаем pip'ы необходимые для работы скрипта get_my_ip.py
os.system("sudo -H pip3 install -r " + str(path_reqairement))
# Устанавливаем supervisor
os.system("sudo apt-get install supervisor -y")
# Редактируем файлы supervisor'a
os.system("sudo touch /etc/supervisor/conf.d/get_my_ip.conf")
sleep(2)
d_1 = [
"[program:get_my_ip]"
]
d_2 = [
"\ncommand=sudo python3 get_my_ip.py"
]
d_3 = [
"\ndirectory=" + str(path)
]
d_4 = [
"\nstdout_logfile=" + str(path) + "/" + "get_my_ip.log"
]
d_5 = [
"\nautostart=true"
]
d_6 = [
"\nautorestart=true"
]
d_7 = [
"\nredirect_stderr=true"
]
data = d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7
with open("/etc/supervisor/conf.d/get_my_ip.conf", "w") as f:
    for d in data:
        f.write(str(d))
sleep(2)
os.system("sudo systemctl enable supervisor.service")
os.system("sudo service supervisor restart")
