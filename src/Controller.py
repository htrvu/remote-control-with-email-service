import os, psutil, uuid
from utils import *
from getmac import get_mac_address as gma

class Controller:
    def __init__(self):
        # self.cmd_dicts = {
        #     'help': self.__show_helps,
        #     'list_apps': self.__list_apps,
        #     'list_processes': self.__list_processes
        # }
        return


    def __process(self, cmd, id = None):
        return
        # if id is None:
        #     cmd_result = self.cmd_dicts[cmd]()
        # else:
        #     cmd_result = self.cmd_dicts[cmd](id)

        # if 'list' in cmd:
        #     data, column_names = cmd_result
        #     return html_table(data, column_names)
        
        # # image data
        # if 'screen' in cmd:
        #     return html_image(cmd_result)

        # # status
        # if 'shut down' in cmd:
        #     pass

        # # other: help,...
        # return cmd_result

    def respond(self, request):
        return
        # words = request.split(' ')

        # if len(words) < 1 or len(words) > 2:
        #     return 'Invalid request'
        
        # cmd, id = words[0], None
        # if len(words) == 2:
        #     id = words[1]
            
        # if cmd not in self.cmd_dicts:
        #     return 'Invalid request'
        
        # return self.__process(cmd, id)
