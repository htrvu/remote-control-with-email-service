
# https://codehandbook.org/how-to-read-email-from-gmail-using-python/

# import smtplib
# from curses.ascii import EM
import imaplib
import email
from utils import *
import email.message
import datetime
from smtplib import SMTP_SSL, SMTP_SSL_PORT

from constants import *

class MailService:
    def __init__(self):
        # self.SMTP_HOST = SMTP_HOST
        # self.SMTP_SERVER = server 
        # self.SMTP_PORT = port
        self.imap_server = imaplib.IMAP4_SSL(IMAP_HOST)
        self.smtp_server = SMTP_SSL(SMTP_HOST, port = SMTP_SSL_PORT)
        # self.smtp_server.set_debuglevel(1)

    def login(self, username, password):
        self.imap_server.login(username, password)
        self.smtp_server.login(username, password)

    def logout(self):
        self.imap_server.logout()
        self.smtp_server.quit()

    def read_email(self, time_from, time_to = datetime.datetime.now().strftime(datetime_format_str()), category = 'primary', box = 'anywhere'):
        mail_list = []

        date_from = datetime.datetime.strptime(time_from, datetime_format_str()).strftime(date_format_str())
        date_to = datetime.datetime.strptime(time_to, datetime_format_str()).strftime(date_format_str())

        try:
            self.imap_server.select('inbox')

            # status, mail_ids = self.imap_server.search(None, f'X-GM-RAW "category:{category} in:{box} after:{date_from} before:{date_to}"')
            # status, mail_ids = self.imap_server.search(None, f'X-GM-RAW "category:{category} in:unread"')
            status, mail_ids = self.imap_server.search(None, f'X-GM-RAW "category:{category}"')

            id_list = mail_ids[0].split()
            if len(id_list) == 0:
                print_color('All mails are read', text_format.OKGREEN)
                return []
            
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id, first_email_id - 1, -1):
                # 'data' will be [(header, content), b')']
                status, data = self.imap_server.fetch(str(i), '(RFC822)')
                
                mail = email.message_from_bytes(data[0][1])

                # date = mail['date']
                # datetime_obj = repr(email.utils.parsedate_to_datetime(repr(date)))

                # if not time_in_range(datetime_obj, time_from, time_to):
                    # continue

                # print_color(f'DATE: {datetime_obj}', text_format.DEBUG)
                
                sender = email.utils.parseaddr(mail['from'])[1]
                subject = mail['subject']
                content = mail['content']

                # Decode subject:
                subject, encoding = email.header.decode_header(subject)[0]
                if encoding:
                    subject = str(subject, encoding)
                
                # Check subject
                # ...
                
                # Decode content:
                # On multipart, we have the text msg and another things like annex, and html version
                # of the msg, in that case we loop through the email payload and get only the plain text
                if mail.is_multipart():
                    content = ''

                    for part in mail.get_payload():
                        if part.get_content_type() == 'text/plain':
                            content += part.get_payload()

                    try:
                        content = base64_decode(content)
                    except Exception as e:
                        print_color('Error at ' + subject + ':\n\t' + str(e), text_format.FAIL)

                mail_list.append({'sender': sender, 'subject': subject, 'content': content})

        except Exception as e:
            print_color('Error while reading the mail inbox:', str(e), text_format.FAIL)
            
        return mail_list

    def send_mail(self, mail):
        try:
            self.smtp_server.sendmail(mail['From'], mail['To'], mail.as_bytes())
        except Exception as e:
            print(e)
            return False
        return True

