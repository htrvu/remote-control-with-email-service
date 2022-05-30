from mail_service import MailService

import threading
import time
import datetime
from services.screen import screen_record, screen_shot
from services.webcam import webcam_record, webcam_shot

from utils import *
from constants import *

from services.help import *
from services.app import *
from services.process import *

from services.html_generator import html_mail
import notification
import signal
from services.explorer import *
from services.mac import *

# demo
from services.help import *

def show_notification_thead(timeout = 60):
    while (True):
        notification.notify (
            title = "Remote control with email service",
            message = "Remote control is running",
            app_name = 'Remote control with email service',
            timeout = 5
        )

        time.sleep(timeout)

host_mail = None

try:
    host_mail = MailService()
    host_mail.login(REMOTE_MAIL, REMOTE_PWD)
except Exception as e:
    print_color('Failed to login with login with name: ' + REMOTE_MAIL, text_format.YELLOW)
    print_color('Full detail below:', text_format.YELLOW)
    
    print_indent(str(e), level = 1, option = text_format.RED)
    exit(1)

def check_email_thread(timeout = 15):
    check_email_thread.keep = True
    
    cfg = load_config()
    try:
        checkpoint = cfg['latest_checkpoint']
        while check_email_thread.keep:
            
            print(f'Reading mail box from {checkpoint} to {datetime.datetime.now()}')
            
            tmp_checkpoint = datetime.datetime.now() - datetime.timedelta(seconds = 10)
            mail_list = host_mail.read_email(time_from = checkpoint)
            checkpoint = tmp_checkpoint
            
            for mail in mail_list:
                print_color('Send from: ' + mail['sender'], text_format.YELLOW)
                print_color('Subject: ' + mail['subject'], text_format.YELLOW)
                print_color('Content: ' + mail['content'], text_format.YELLOW)
                print_color('-------------------------------------------------------------------------', text_format.OKGREEN)
            
            time.sleep(timeout)
    except KeyboardInterrupt:
        print_color('Stop checking mail box', text_format.OKGREEN)
    
    print_color(f'Checkpoint saving at {checkpoint}', text_format.OKGREEN)
    update_config_value('latest_checkpoint', checkpoint)

def stop_reading_mail(signum, frame):
    check_email_thread.keep = False

signal.signal(signal.SIGTERM, stop_reading_mail)

def check_missing_thread(timeout = 300):
    pass

def setup():
    pass

def main():
    threading.Thread(target = check_email_thread).start()

    ##############################################################
    # Test read mail
    # mails = host_mail.read_email(time_from='2022-04-20 00:00:00')
    
    # print_color('Test read inbox', text_format.OKGREEN)
    # for mail in mails:
    #     print('From:', mail['sender'])
    #     print('Subject:', mail['subject'])
    #     print('Content:', mail['content'])
    #     print('---------------------------------')
    #     break

    ##############################################################
    # Test send mail
    # print_color('Test send mail', text_format.OKGREEN)
    '''
    try:
        # html = show_helps()
        # request = 'HELP'

        # html = get_apps()
        # request = 'APP get'

        html = get_processes()
        request = 'PROCESS get'

        content = html_mail(request, html)

        mail = build_email_content(REMOTE_MAIL, ['hoangnhuquynh2015@gmail.com'], 'Demo send mail', content)
        host_mail.send_mail(mail)
    except Exception as e:
        print_color('Error while sending mail: ' + str(e), text_format.FAIL)
    
    print_color('Mail sent', text_format.OKGREEN)
    '''
    ##############################################################
    # Test thread

    # _show_notification_thead = threading.Thread(target = show_notification_thead, args = ())
    # _check_email_thread = threading.Thread(target = check_email_thread, args = ())
    
    # _check_email_thread.start()
    # _show_notification_thead.start()

    # _check_email_thread.join()
    # _show_notification_thead.join()

    # email = Email()

    ##############################################################
    # Pipeline
    # while True:
    #     mails = email.read_email()
    #     for mail in mails:
    #         # new thread to process this request       


if __name__ == '__main__':
    main()
