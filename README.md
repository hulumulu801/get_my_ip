Я использовал python3. Тестировал скрипт на Ubuntu 20.04 LTS Descktop & Ubuntu 20.04 LTS 
Server!

# Как установить:
  - устанавливаем git clone:
    
        sudo apt install git

  - проверяем, есть ли python3:
  
        python3 -V

        если нет, то устанавливаем
 
  - устанавливаем pip:
  
        sudo apt install python3-pip
    
   - открываем файл get_my_ip.py любым текстовым редактором и изменяем строки:
   
    addr_from = "" - сюды пишем от какой почты будем получать письма
    password = "" - тут, пароль от почты, что указали сверху
    addr_to = "" - сюде пишем, на какую почту нам будут ссыпаться письма
    sleep(180) - в скобках указываем время(в секундах), через сколько будут ссыпаться письма, по умолчанию 180 сек.

![Image alt](https://github.com/hulumulu801/get_my_ip/blob/master/pict/pict_1.png)
![Image alt](https://github.com/hulumulu801/get_my_ip/blob/master/pict/pict_2.png)

   **Важно!!! С той почты, с которой будут отправляться письма в настройках аккаунта(вкладка "Безопасность") разрешить доступ "Ненадежные приложения, у которых есть доступ к аккаунту"**
   
![Image alt](https://github.com/hulumulu801/get_my_ip/blob/master/pict/pict_3.png)
