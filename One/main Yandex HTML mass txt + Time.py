
import openpyxl
import random
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.image import MIMEImage   



print('Начинаем работу... \n')
global recipient_list
import time
start_time = time.time()
recipient_list = []
def send_email():
	with open('recipient_list.txt', 'r', encoding='utf-8') as f:
		for addr_to in f:
			addr_to = addr_to.replace('[', '').replace('\'', '').replace(']', '').replace('\n', '')

			recipient_list.append(addr_to)
			print(addr_to)

			with open("email_template.html") as file:
				html = file.read()
				
			addr_from = ""                 # Адресат                   # Получатель
			password  = ""                                  # Пароль
			msg = MIMEMultipart()                               # Создаем сообщение
			msg['From']    = addr_from                          # Адресат
			msg['To']      = addr_to                            # Получатель
			msg['Subject'] = 'WOWTILE'                      # Тема сообщения  
			msg.attach(MIMEText(html, 'html', 'cp1251'))         # Добавляем в сообщение текст
			server = smtplib.SMTP('smtp.yandex.com')           # Создаем объект SMTP
			server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
			server.starttls()                                   # Начинаем шифрованный обмен по TLS
			server.login(addr_from, password)                   # Получаем доступ
			server.send_message(msg)                            # Отправляем сообщение
			server.quit()                                       # Выходим
			print('Сообщение на адрес', addr_to, 'отправлено')
def main():
    print(send_email())


if __name__ == "__main__":
    main()

print("--- %s seconds ---" % (time.time() - start_time))
