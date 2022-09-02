import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект

with open("email_template.html") as file:
			html = file.read()


book = openpyxl.open('sender_base.xlsx', read_only = True)
sheet = book.active
for i in range(1, sheet.max_row+1):
    # desk_email = sheet[i][0].value
    desk_email = sheet.cell(row=i, column=1).value
    # desk_email = cell_obj.value

    addr_to = desk_email
    addr_from = "wtile.info@yandex.ru"                 # Адресат                   # Получатель
    password  = "fhqfgletedtmheao"                                  # Пароль
    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'НОВЫЙ ГОД'                      # Тема сообщения  
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение текст
    server = smtplib.SMTP('smtp.yandex.com')           # Создаем объект SMTP
    server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим
    print('Сообщение на адрес', addr_to, 'отправлено')