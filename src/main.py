from urllib import response
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
from services.explorer import *
from services.mac import *

from services.html_generator import html_mail

# demo
from services.help import *

# test lib
import imghdr

def show_notification_thead(timeout = 60):
    pass
    # while (True):
    #     notification.notify (
    #         title = "Remote control with email service",
    #         message = "Remote control is running",
    #         app_name = 'Remote control with email service',
    #         timeout = timeout / 2
    #     )

    #     time.sleep(timeout)

def check_email_thread(timeout = 10):
    while (True):
        print('ahihi')
        time.sleep(timeout)

def check_missing_thread(timeout = 300):
    pass

def setup():
    pass


def main():
    host_mail = MailService()
    host_mail.login(REMOTE_MAIL, REMOTE_PWD)

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
    print_color('Test send mail', text_format.OKGREEN)

    try:
        # request = 'MAC get'
        # result = get_mac()

        request = 'HELP'
        result = show_helps()

        # request = 'APP get'
        # result = get_apps()

        # request = 'PROCESS get'
        # result = get_processes()

        # id = '6712'
        # request = f'APP close {id}'
        # result = close_app(id)

        # src = 'C:\\Users\\Admin\\Downloads\\demo2'
        # dst = 'C:\\Users\\Admin\\Downloads\\hihi'
        # html = copy(src, dst)
        # request = f'COPY {src} {dst}'

        # src = 'C:\\Users\\Admin\\Downloads\\demo1\demo1_1.txt'
        # dst = 'C:\\Users\\Admin\\Downloads\\hehe\\whatup.txt'
        # html = cut(src, dst)
        # request = f'CUT {src} {dst}'

        # path = 'C:\\Users\\Admin\\Downloads\\demo1\demo1_2.txt'
        # html = delete(path)
        # request = f'DELETE {path}'

        # html = show_tree('C:\\Users\\Admin\\Downloads\demo1')
        # request = 'TREE C:\\Users\\Admin\\Downloads\demo1'

        # data, msg = screen_shot()
        # request = 'SCREEN get image'

        # result = webcam_shot()
        # request = 'WEBCAM get image'

        # result = webcam_record(5)
        # request = 'WEBCAM get video 5'

        content = {
            'html': html_mail(request, result['html']),
            'data': result['data']
        }
        
        mail = build_email_content(REMOTE_MAIL, ['hoangnhuquynh2015@gmail.com'], 'Demo send mail', content)
        # mail = build_email_content(REMOTE_MAIL, ['bot.remote.2@gmail.com'], 'Demo WEBCAM video attachment', content)
        host_mail.send_mail(mail)

        # mail = build_email_content(REMOTE_MAIL, ['bot.remote.2@gmail.com'], 'Demo PNG attachment', content, data = data)
        # host_mail.send_mail(mail)
    except Exception as e:
        print_color('Error while sending mail: ' + str(e), text_format.FAIL)
    
    print_color('Mail sent', text_format.OKGREEN)

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

