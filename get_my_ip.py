#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
import requests
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
from fake_useragent import UserAgent
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#######################################################################################################################
def get_my_ip_html(url):
    try:
        header = {
                    "User-Agent": UserAgent().chrome
        }
        r = requests.get(url, headers = header)
        if str(r) == "<Response [200]>":
            return r.text
    except Exception as e:
        pass
#######################################################################################################################
def get_my_ip(my_ip_html):
    try:
        soup = BeautifulSoup(my_ip_html, "lxml")
        div = soup.find("div", class_ = "services_find_ip services").find("div", class_ = "ip_block").find("div", class_ = "ip")
        get_ip = str(div).split(">")[-2].split("<")[0]
        return get_ip
    except Exception as e:
        pass
#######################################################################################################################
def send_message(my_ip):
    try:
        addr_from = "" # Адресат
        password = "" # Пароль
        addr_to = "" # Получатель

        msg = MIMEMultipart()                               # Создаем сообщение
        msg['From']    = addr_from                          # Адресат
        msg['To']      = addr_to                            # Получатель
        msg['Subject'] = "Твой IP"                          # Тема сообщения

        body = "Время: " + str(datetime.now()) + "\nIP: " + str(my_ip)
        msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

        server = smtplib.SMTP('smtp.gmail.com', 587)        # Создаем объект SMTP
        server.starttls()                                   # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)                   # Получаем доступ
        server.send_message(msg)                            # Отправляем сообщение
        server.quit()
    except Exception as e:
        pass
#######################################################################################################################
while True:
    url = "https://hidemy.name/ru/ip/"
    my_ip = get_my_ip(get_my_ip_html(url))
    send_message(my_ip)
    sleep(180)
