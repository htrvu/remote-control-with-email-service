import time
from utils import *
from constants import *

from plyer import notification

from responder import respond
import threading

def show_notification_thread(timeout = 300):
    while True:
        notification.notify (
            title = "Remote control with email service",
            message = "Remote control is running",
            app_name = 'Remote control with email service',
            app_icon = 'ui/assets/icons/remote_logo.ico',
            timeout = 5
        )

        time.sleep(timeout)

def check_email_thread(host_mail, timeout = 15):   
    try:
        while True:
            print('Reading unread mails in primary mail box...')
            
            mail_list = host_mail.read_email()

            for mail in mail_list:
                mail['subject'] = mail['subject'].replace('\n', '')
                mail['subject'] = mail['subject'].replace('\r', '')
                print_color('Send from: ' + mail['sender'], text_format.YELLOW)
                print_color('Subject: ' + mail['subject'], text_format.YELLOW)
                print_color('-------------------------------------------------------------------------', text_format.OKGREEN)
                process_thread = threading.Thread(target = respond, args = (host_mail, mail, ))
                process_thread.daemon = True
                process_thread.start()
            
            time.sleep(timeout)
    except KeyboardInterrupt:
        print_color('Stop checking mail box', text_format.OKGREEN)