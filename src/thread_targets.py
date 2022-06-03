import time
from utils import *
from constants import *

from plyer import notification

from responder import respond
import threading

import app_logging as logging

def show_notification_thread(timeout = 300):
    logging.log('Notification thread is running')
    while True:
        notification.notify (
            title = "Remote Control with Email Service",
            message = "Remote Control is running",
            app_name = 'Remote Control with Email Service',
            app_icon = 'ui/assets/icons/remote_logo.ico',
            timeout = 5
        )

        time.sleep(timeout)
        
def logging_thread(logfilepath = './g8rc.log', timeout = 5):
    logging.set_log_file_path(logfilepath)
    logging.log(f'Log file location {os.path.join(os.getcwd(), logfilepath)}')
    logging.log('Logging thread is running')
    while True:
        logging.save()
        time.sleep(timeout)

def check_email_thread(host_mail, timeout = 15):
    logging.log('Check mail thread is running')
    try:
        while True:
            print('Reading unread mails in primary mail box...')
            
            mail_list = host_mail.read_email()

            for mail in mail_list:
                mail['subject'] = mail['subject'].replace('\n', '')
                mail['subject'] = mail['subject'].replace('\r', '')
                print_color('Send from: ' + mail['sender'], text_format.YELLOW)
                print_color('Subject: ' + mail['subject'], text_format.YELLOW)
                print_color('-' * 40, text_format.OKGREEN)
                process_thread = threading.Thread(target = respond, args = (host_mail, mail, ))
                process_thread.daemon = True
                process_thread.start()
            
            time.sleep(timeout)
    except KeyboardInterrupt:
        logging.log('Stop checking mail box')
        print_color('Stop checking mail box', text_format.OKGREEN)