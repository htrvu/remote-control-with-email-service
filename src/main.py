import signal

from utils import *
from constants import *
from thread_targets import *

from mail_service import MailService
from remote_control import RemoteControl

def main():
    host_mail = None
    try:
        host_mail = MailService()
        host_mail.login(REMOTE_MAIL, REMOTE_PWD)
    except Exception as e:
        print_color('Failed to login with login with name: ' + REMOTE_MAIL, text_format.YELLOW)
        print_color('Full detail below:', text_format.YELLOW)
        
        print_indent(str(e), level = 1, option = text_format.RED)
        exit(1)
    
    signal.signal(signal.SIGTERM, stop_reading_mail)

    RemoteControl(host_mail).start()

    # checking_thread = threading.Thread(target = check_email_thread, args = (host_mail, ))
    # checking_thread.start()
    # threading.Thread(target = show_notification_thead, args = ()).start()
    
    # checking_thread.join()
    # if host_mail:
        # host_mail.logout()

if __name__ == '__main__':
    main()