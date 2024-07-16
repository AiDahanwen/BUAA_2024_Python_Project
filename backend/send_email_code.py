import smtplib
import string
from email.mime.text import MIMEText
import random

from database import get_constant

send_by = '2892278592@qq.com'
email_password = 'kwniejavvatkdgcf'
mail_host = 'smtp.qq.com'
send_port = 465
file_name = 'send_email_code.py'


def update_constants():
    global send_by
    global email_password
    global mail_host
    global send_port
    
    send_by = get_constant(file_name, 'send_by')
    email_password = get_constant(file_name, 'email_password')
    mail_host = get_constant(file_name, 'mail_host')
    send_port = get_constant(file_name, 'send_port')


def get_code(n=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))


def send_email(send_to, content, subject='验证码'):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = send_by
    msg['To'] = send_to
    msg['Subject'] = subject
    
    smtp = smtplib.SMTP_SSL(mail_host, send_port)
    smtp.login(send_by, email_password)
    smtp.sendmail(send_by, send_to, msg.as_string())
    smtp.close()


def send_email_code(send_to):
    update_constants()
    verify_code = get_code()
    content = '【验证码】您的验证码是：' + verify_code + ' 。若非本人操作，请忽略这条信息。'
    try:
        send_email(send_to, content)
        return verify_code
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    print(send_email_code('2892278592@qq.com'))
