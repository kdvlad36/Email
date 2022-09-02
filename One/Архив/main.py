from email import message
import smtplib as smtp
import os
from email.mime.text import MIMEText

subject = "HOOLY"
email_text = "HI"

def send_email(message):
    email = "wtile.info@yandex.ru"
    password = "fhqfgletedtmheao"
    dest_email = 'wtile.info@yandex.ru'
    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.login(email, password)
    server.ehlo(email)
    server.auth_plain()
   
    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                       dest_email,
                                                       subject,
                                                       email_text)
    server.sendmail(email, dest_email, message)
    server.quit()
    
    try:
        
        

        return "Сообщение успешно отправлено!"
    except Exception as _ex:
        return f"{_ex}\nПожалуйста, проверьте ваш логин или пароль!"


def main():
    print(send_email(message=message))



if __name__ == "__main__":
    main()
