from email import Email
import threading
import time
from utils import *
from constants import *

def show_notification_thead(timeout = 60):
    while (True):
        notification.notify (
            title = "Remote control with email service",
            message = "Remote control is running",
            app_name = 'Remote control with email service',
            timeout = timeout / 2
        )

        time.sleep(timeout)

def check_email_thread(timeout = 10):
    while (True):
        print('ahihi')
        time.sleep(timeout)

def check_missing_thread(timeout = 300):
    pass

def setup():
    pass



def main():
    # gmail = Email('imap.gmail.com', 993)
    host_mail = Email()
    host_mail.login(REMOTE_MAIL, REMOTE_PWD)

    # controller = Controller()

    # VDT help
    # VDT list_apps
    # VDT list_processes
    # VDT shut_down
    # subjects, contents = gmail.read_email()
    # subjects = ['VDT help', 'VDT list_apps']
    # for subject in subjects:
    #     if not subject.startswith(CMD_ID):
    #         continue
    
    #     request = subject[len(CMD_ID):]
    #     respond = controller.respond(request)
    #     print(respond)

    # _show_notification_thead = threading.Thread(target = show_notification_thead, args = ())
    # _check_email_thread = threading.Thread(target = check_email_thread, args = ())
    
    # _check_email_thread.start()
    # _show_notification_thead.start()

    # _check_email_thread.join()
    # _show_notification_thead.join()

    # email = Email()

    # while True:
    #     mails = email.read_email()
    #     for mail in mails:
    #         # new thread to process this request       


if __name__ == '__main__':
    main()