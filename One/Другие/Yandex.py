from email.mime.text import MIMEText
import smtplib as smtp
import os
from getpass import getpass


try:
    with open("email_template.html") as file:
        template = file.read()
except IOError:



email = 'wtile.info@yandex.ru'
password = 'fhqfgletedtmheao'
dest_email = 'wtile.info@yandex.ru'
subject = input('тема письма: \n')
email_text = input('текст письма: \n' )

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                       dest_email,
                                                       subject,
                                                       email_text)

server = smtp.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()