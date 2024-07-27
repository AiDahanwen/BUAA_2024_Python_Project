import random
import re
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from backend.database import get_constant_info

send_by = '3498314162@qq.com'
email_password = 'rkkemgvqthnachie'
mail_host = 'smtp.qq.com'
send_port = 465
file_name = 'send_email_code.py'


def update_constants():
    global send_by
    global email_password
    global mail_host
    global send_port

    send_by = get_constant_info(file_name, 'send_by')
    email_password = get_constant_info(file_name, 'email_password')
    mail_host = get_constant_info(file_name, 'mail_host')
    send_port = get_constant_info(file_name, 'send_port')


def get_code(n=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))


def send_email(send_to, verify_code, subject='Email Verification Code'):
    with open('./backend/html_content.html', 'r', encoding='utf-8') as file:
        html_content = file.read().replace("verify_code", str(verify_code))

    msg = MIMEMultipart('alternative')
    msg['From'] = send_by
    msg['To'] = send_to
    msg['Subject'] = subject

    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)

    smtp = smtplib.SMTP_SSL(mail_host, send_port)
    smtp.login(send_by, email_password)
    smtp.sendmail(send_by, send_to, msg.as_string())
    smtp.close()


def send_email_code(send_to):
    update_constants()
    verify_code = get_code()
    try:
        send_email(send_to, verify_code)
        return verify_code
    except Exception as e:
        print(e)
        return False


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == '__main__':
    print(send_email_code('2892278592@qq.com'))
