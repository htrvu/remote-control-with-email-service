import base64
import email.message

def base64_decode(str):
    str = base64.b64decode(str)
    return str.decode('utf-8')

def build_email_content(mail_from, mail_to, header, body):
    email_message = email.message.EmailMessage()
    email_message.add_header('To', ', '.join(mail_to))
    email_message.add_header('From', mail_from)
    email_message.add_header('Subject', header)
    email_message.add_header('X-Priority', '1')  # Urgency, 1 highest, 5 lowest
    email_message.set_content(body)
    return email_message

def show_notify():
    pass