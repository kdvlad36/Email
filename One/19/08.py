# import module
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект

with open("email_template.html") as file:
			html = file.read()

wrkbk = openpyxl.load_workbook("sender_base.xlsx", read_only = True)
sh = wrkbk.active
email = []
	
for j in range(1, sh.max_column+1):
    addr_to = j
    addr_from = "wtile.info@yandex.ru"                 # Адресат                   # Получатель
    password  = ""                                  # Пароль
    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = j                            # Получатель
    msg['Subject'] = 'НОВЫЙ ГОД'                      # Тема сообщения  
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение текст
    server = smtplib.SMTP('smtp.yandex.com')           # Создаем объект SMTP
    server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим
    print('Сообщение на адрес', j, 'отправлено')

