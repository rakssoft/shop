from django.test import TestCase

# Create your tests here.


import smtplib                                              # Импортируем библиотеку по работе с SMTP
import os                                                   # Функции для работы с операционной системой, не зависящие от используемой
fromaddr = 'FaustRF@yandex.ru'
toaddrs  = 'rfm8z@region.komus.net'
msg = 'There was a terrible error that occured and I wanted you to know!'


    # Credentials (if needed)
username = 'FaustRF@yandex.ru'
password = 'qazwsxedcr123'
print("0")
    # The actual mail send
server = smtplib.SMTP('smtp.yandex.ru', 465)
#server = smtplib.SMTP(host='smtp.yandex.ru', port=465)
print("1")


server.starttls()
print("2")
server.login(username,password)
print("3")
server.sendmail(fromaddr, toaddrs, msg)
print("4")
server.quit()
print("5")