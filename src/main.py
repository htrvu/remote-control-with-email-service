from utils import *
from constants import *
from thread_targets import *

from remote_control import RemoteControl

import global_variables
import colorama
import app_logging as logging   

def setup():
    threading.Thread(target = logging_thread, args = ('./g8rc.log', 5, ), daemon = True).start()
    cfg = load_config('./configs/app_configs.yaml')

    global_variables.app_configs['white_list'] = cfg['white_list']
    global_variables.app_configs['auto_run'] = cfg['auto_run']

def main():
    setup()
    RemoteControl().start()

if __name__ == '__main__':
    main()