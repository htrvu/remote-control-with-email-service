import threading
import time
import utils
import Email
from plyer import notification

from utils import *

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
    _show_notification_thead = threading.Thread(target = show_notification_thead, args = ())
    _check_email_thread = threading.Thread(target = check_email_thread, args = ())
    
    _check_email_thread.start()
    _show_notification_thead.start()

    _check_email_thread.join()
    _show_notification_thead.join()

if __name__ == '__main__':
    main()