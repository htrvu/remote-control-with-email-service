import time
import datetime
from utils import *
from constants import *

from plyer import notification

from responder import respond
import threading

def show_notification_thead(timeout = 60):
    while (True):
        notification.notify (
            title = "Remote control with email service",
            message = "Remote control is running",
            app_name = 'Remote control with email service',
            timeout = 5
        )

        time.sleep(timeout)

def check_email_thread(host_mail, timeout = 15):
    check_email_thread.keep = True
    
    cfg = load_config()
    try:
        checkpoint = cfg['latest_checkpoint']
        while check_email_thread.keep:
            
            print(f'Reading mail box from {checkpoint} to {datetime.datetime.now()}')
            
            tmp_checkpoint = datetime.datetime.now() - datetime.timedelta(seconds = 8)
            mail_list = host_mail.read_email(time_from = checkpoint)
            checkpoint = tmp_checkpoint
            
            update_config_value('latest_checkpoint', checkpoint)
            
            for mail in mail_list:
                print_color('Send from: ' + mail['sender'], text_format.YELLOW)
                print_color('Subject: ' + mail['subject'], text_format.YELLOW)
                print_color('-------------------------------------------------------------------------', text_format.OKGREEN)
                threading.Thread(target = respond, args = (host_mail, mail, )).start()
            
            time.sleep(timeout)
    except KeyboardInterrupt:
        print_color('Stop checking mail box', text_format.OKGREEN)
    

def stop_reading_mail(signum, frame):
    check_email_thread.keep = False