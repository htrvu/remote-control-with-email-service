
# https://codehandbook.org/how-to-read-email-from-gmail-using-python/

# import smtplib
import imaplib
import email
# import base64
from utils import *

class Email:
    def __init__(self, server, port):
        self.SMTP_SERVER = server 
        self.SMTP_PORT = port
        self.mail = imaplib.IMAP4_SSL(server)

    def login(self, username, password):
        self.mail.login(username, password)

    # add more features
    def read_email(self):
        try:
            self.mail.select('inbox')

            _, mail_ids = self.mail.search(None, 'ALL')
        
            id_list = mail_ids[0].split()

            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            cnt = 0
            for i in range(latest_email_id, first_email_id - 1, -1):
                # 'data' will be [(header, content), b')']
                _, data = self.mail.fetch(str(i), '(RFC822)')

                msg = email.message_from_bytes(data[0][1])
                
                subject = msg['subject']
                content = msg['content']

                # base64 decode for subject
                if subject.startswith('=?UTF-8?'):
                    subject = subject.split('?')[-2]
                    subject = base64_decode(subject)

                # base64 decode for subject
                if msg.is_multipart():
                    content = ''
                    # on multipart we have the text msg and another things like annex, and html version
                    # of the msg, in that case we loop through the email payload
                    for part in msg.get_payload():
                        # if the content type is text/plain, we extract it
                        if part.get_content_type() == 'text/plain':
                            content += part.get_payload()

                    content = base64_decode(content)

                print(subject)
                print(content)

        except Exception as e:
            print('Error! ', end='')
            print(str(e))


if __name__ == '__main__':
    EMAIL = "bot.remote.1@gmail.com"
    PWD = "yiggxtcpnmegepuu"
    gmail = Email('imap.gmail.com', 993)
    gmail.login(EMAIL, PWD)
    gmail.read_email()