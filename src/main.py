from utils import *
from constants import *
from thread_targets import *

from mail_service import MailService
from remote_control import RemoteControl

import global_variables

def setup():
    cfg = load_config('./configs/app_configs.yaml')

    global_variables.app_configs['white_list'] = cfg['white_list']
    global_variables.app_configs['auto_run'] = cfg['auto_run']

def main():
    setup()

    host_mail = None
    try:
        print_color('Login to mail server...', text_format.OKGREEN)
        host_mail = MailService()
        host_mail.login(REMOTE_MAIL, REMOTE_PWD)
        print_color('Login successfully', text_format.OKGREEN)
    except Exception as e:
        print_color('Failed to login with login with name: ' + REMOTE_MAIL, text_format.YELLOW)
        print_color('Full detail below:', text_format.YELLOW)
        
        print_indent(str(e), level = 1, option = text_format.RED)
        exit(1)
    
    RemoteControl(host_mail).start()

if __name__ == '__main__':
    main()  