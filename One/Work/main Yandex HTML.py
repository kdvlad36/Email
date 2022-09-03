import smtplib                                      # Импортируем библиотеку по работе с SMTP
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения

with open("email_template.html") as file:
    html = file.read()

addr_from = ""                 # Адресат
addr_to   = ""                   # Получатель
password  = ""                                  # Пароль

msg = MIMEMultipart()                               # Создаем сообщение
msg['From']    = addr_from                          # Адресат
msg['To']      = addr_to                            # Получатель
msg['Subject'] = 'НОВЫЙ ГОД'                      # Тема сообщения

#body = "Приглашаем на новый год"
#msg.attach(MIMEText(body, 'plain'))   
msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение текст

server = smtplib.SMTP('smtp.yandex.com')           # Создаем объект SMTP
server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
server.starttls()                                   # Начинаем шифрованный обмен по TLS
server.login(addr_from, password)                   # Получаем доступ
server.send_message(msg)                            # Отправляем сообщение
server.quit()                                       # Выходим
