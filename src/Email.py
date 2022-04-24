
# https://codehandbook.org/how-to-read-email-from-gmail-using-python/

# import smtplib
# from curses.ascii import EM
import imaplib
import email
from utils import *
import email.message
import datetime
from smtplib import SMTP_SSL, SMTP_SSL_PORT
# from Controller import *

class Email:
    def __init__(self, server, port):
        SMTP_HOST = 'smtp.googlemail.com'
        self.SMTP_SERVER = server 
        self.SMTP_PORT = port
        self.mail = imaplib.IMAP4_SSL(server)
        self.smtp_server = SMTP_SSL(SMTP_HOST, port = SMTP_SSL_PORT)
        self.smtp_server.set_debuglevel(1)

    def login(self, username, password):
        self.mail.login(username, password)
    
    def connect_to_smtp(self, username, passowrd):
        self.smtp_server.login(username, passowrd)

    def logout_imap(self):
        self.mail.logout()

    def logout_smtp(self):
        pass

    # add more features
    def read_email(self, time_from, time_to = datetime.datetime.now().strftime(datetime_format_str()), category = 'primary', box = 'anywhere'):
        mail_list = []

        date_from = datetime.datetime.strptime(time_from, datetime_format_str()).strftime(date_format_str())
        date_to = datetime.datetime.strptime(time_to, datetime_format_str()).strftime(date_format_str())

        try:
            self.mail.select('inbox')

            status, mail_ids = self.mail.search(None, f'X-GM-RAW "category:{category} in:{box} after:{date_from} before:{date_to}"') # specify the primary category

            id_list = mail_ids[0].split()
            if len(id_list) == 0:
                print_color('All mails are read', text_format.OKGREEN)
                return []
            
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id, first_email_id - 1, -1):
                # 'data' will be [(header, content), b')']
                status, data = self.mail.fetch(str(i), '(RFC822)')

                date = email.message_from_bytes(data[0][1])['date']
                datetime_obj = repr(email.utils.parsedate_to_datetime(repr(date)))

                if not time_in_range(datetime_obj, time_from, time_to):
                    continue

                print_color(f'DATE: {datetime_obj}', text_format.DEBUG)

                msg = email.message_from_bytes(data[0][1])
                
                subject = msg['subject']
                content = msg['content']

                # decode subject
                subject, encoding = email.header.decode_header(subject)[0]
                if encoding:
                    subject = str(subject, encoding)

                # decode content
                if msg.is_multipart():
                    content = ''
                #     # on multipart we have the text msg and another things like annex, and html version
                #     # of the msg, in that case we loop through the email payload
                    for part in msg.get_payload():
                #         # if the content type is text/plain, we extract it
                        if part.get_content_type() == 'text/plain':
                            content += part.get_payload()
                    try:
                        content = base64_decode(content)
                    except Exception as e:
                        print_color('Error at ' + subject, text_format.FAIL)

                    try:
                        content = base64_decode(content)
                    except Exception as e:
                        print_color(str(e), text_format.FAIL)

                mail_list.append({'subject': subject, 'content': content})
                
        except Exception as e:
            print_color('Something went wrong while checking the mail box', text_format.FAIL)
            print(str(e))
            
        return mail_list

    def send_mail(self, _email):
        try:
            self.smtp_server.sendmail(_email['From'], _email['To'], _email.as_bytes())
        except Exception as e:
            print(e)
            return False
        return True

    def build_email_content(mail_from, mail_to, header, body, format = 'html'):
        email_message = email.message.EmailMessage()
        email_message.add_header('To', ', '.join(mail_to))
        email_message.add_header('From', mail_from)
        email_message.add_header('Subject', header)
        email_message.add_header('X-Priority', '1')  # Urgency, 1 highest, 5 lowest
        email_message.set_content(body, format)
        return email_message
