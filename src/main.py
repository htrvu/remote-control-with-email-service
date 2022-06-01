from requests import request
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
from services.keylogger import *
from services.pc import *
from services.registry import *

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
    # threading.Thread(target = check_email_thread).start()

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
        # html = show_helps()
        # request = 'HELP'

        # html = get_apps()
        # request = 'APP get'

        # html = get_processes()
        # request = 'PROCESS get'

        # request = 'KEYLOGGER 10'
        # result = get_key_log(10)

        # request = 'PC restart'
        # result = restart()

        # registry_path = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Mozilla\\Mozilla Firefox\\100.0.2 (x64 vi)\\Uninstall\\Description'
        # request = 'REGISTRY get ' + registry_path
        # result = get_value(registry_path)

        # registry_path = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Mozilla\\Mozilla Firefox\\100.0.2 (x64 vi)\\Uninstall\\AddNewKey'
        # registry_path = 'HKEY_CLASSES_ROOT\\Word.Picture\\AddNewKey'
        # registry_path = 'HKEY_USERS\\.DEFAULT\\Software\\AddNewKey'
        # registry_path = 'HKEY_CURRENT_CONFIG\\Software\\Fonts\\AddNewKey'
        registry_path = 'HKEY_CURRENT_USER\\SOFTWARE\\Wireshark\\WinSparkle Settings\\AddNewKey\\Testing'

        # request = 'REGISTRY add_key ' + registry_path
        # result = add_key(registry_path)

        # request = 'REGISTRY add_value ' + registry_path
        # result = add_value(registry_path, 'TestAddValue nek', 'REG_SZ')

        # request = 'REGISTRY modify ' + registry_path
        # result = modify_value(registry_path, 'Being modified', 'REG_SZ')

        request = 'REGISTRY add_value ' + registry_path
        result = add_value(registry_path, '19835135', 'REG_DWORD')

        # request = 'REGISTRY delete_value ' + registry_path
        # result = delete_value(registry_path)

        # request = 'REGISTRY delete_key ' + registry_path
        # result = delete_key(registry_path)

        content = {
            'html': html_mail(request, result['html']),
            'data': result['data']
        }

        # content = html_mail(request, html)

        mail = build_email_content(REMOTE_MAIL, ['bot.remote.2@gmail.com'], 'Demo add_value REG_DWORD registry', content)
        host_mail.send_mail(mail)
        print_color('Mail sent', text_format.OKGREEN)
    except Exception as e:
        print_color('Error while sending mail: ' + str(e), text_format.FAIL)
    
    
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
