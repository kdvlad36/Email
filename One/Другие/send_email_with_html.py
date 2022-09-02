from email.mime.text import MIMEText
import smtplib as smtp
import os
from getpass import getpass


def send_email():
    email = "wtile.info@yandex.ru"
    # your password = "your password"
    password = "fhqfgletedtmheao"
    dest_email = 'wtile.info@yandex.ru'
    subject = ('тема письма: \n')
    email_text = input('текст письма: \n' )

    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                       dest_email,
                                                       subject,
                                                       email_text)

    try:
        with open("email_template.html") as file:
            template = file.read()
    except IOError:
        return "The template file doesn't found!"

    try:
        server = smtp.SMTP_SSL('smtp.yandex.com')
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.auth_plain()
        server.sendmail(email, dest_email, message)
        server.quit()

        return "Сообщение успешно отправлено!"
    except Exception as _ex:
        return f"{_ex}\nПожалуйста, проверьте ваш логин или пароль!"



def main():
    print(send_email())


if __name__ == "__main__":
    main()
