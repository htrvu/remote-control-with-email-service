'''
    split thread
'''

from Email import Email
from Controller import Controller
from utils import *

def show_notification_thead(timout = 300):
    pass

def check_email_thread(timout = 30):
    pass

def check_missing_thread(timeout = 300):
    '''
        @todo
        - check the internet connection
        - check config file
        - check checkpoint file
    '''
    pass

def main_process():
    pass

def setup():
    pass



def main():
    CMD_ID = 'VDT'
    # EMAIL = "bot.remote.1@gmail.com"
    # PWD = "yiggxtcpnmegepuu"
    # gmail = Email('imap.gmail.com', 993)
    # gmail.login(EMAIL, PWD)

    controller = Controller()

    # VDT help
    # VDT list_apps
    # VDT list_processes
    # VDT shut_down
    # subjects, contents = gmail.read_email()
    subjects = ['VDT help', 'VDT list_apps']
    for subject in subjects:
        if not subject.startswith(CMD_ID):
            continue
    
        request = subject[len(CMD_ID):]
        respond = controller.respond(request)
        print(respond)


        




if __name__ == '__main__':
    main()