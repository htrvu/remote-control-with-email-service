import os, psutil, uuid
from utils import *
from getmac import get_mac_address as gma

class Controller:
    def __init__(self):
        self.cmd_dicts = {
            'help': self.__show_helps,
            'list_apps': self.__list_apps,
            'list_processes': self.__list_processes,
            # 'shut_down': self.__shut_down
        }

    def __show_helps(self):
        return '''
            ------ Remote control app with Email service ------
            Authors:
                Hoang Trong Vu
                Tran Ngoc Do
                Tran Huu Thien

            Command list:
                VDT help                show helps
                VDT list_apps           list the running apps
                VDT list_processes      list the running process
                VDT shut_down           shut down the computer
                ...                     ...
        '''

    def __list_apps(self):
        cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
        ps_result = os.popen(cmd).read().split('\n')

        # names, ids, threads = [], [], []
        
        column_names = ['No.', 'Description', 'Id', 'ThreadCount']
        data = []

        no = 1
        for line in ps_result[3:]:
            if line.isspace() or len(line) == 0:
                continue

            arr = line.split(" ")

            # thread count
            thread_count = arr[-1]

            # id
            pos = len(arr) - 2
            for i in range(pos, -1, -1):
                if len(arr[i]) != 0:
                    id = arr[i]
                    pos = i
                    break

            name = ''
            for i in range(0, pos):
                if len(arr[i]) != 0:
                    name = name + arr[i] + ' '
            name = name[:-1]

            data.append([no, name, id, thread_count])
            no += 1

        return data, column_names

    def __list_processes(self):
        column_names = ['No.', 'Description', 'Id', 'ThreadCount']
        data = []

        no = 1
        for process in psutil.process_iter():
            try:
                data.append([no, process.name(), process.pid, process.num_threads()])
                no += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return data, column_names

    def __screen_shot(self):
        # return base64 encoded image
        pass

    def __process(self, cmd, id = None):
        if id is None:
            cmd_result = self.cmd_dicts[cmd]()
        else:
            cmd_result = self.cmd_dicts[cmd](id)

        if 'list' in cmd:
            data, column_names = cmd_result
            return html_table(data, column_names)
        
        # image data
        if 'screen' in cmd:
            return html_image(cmd_result)

        # status
        if 'shut down' in cmd:
            pass

        # other: help,...
        return cmd_result

    def respond(self, request):
        words = request.split(' ')

        if len(words) < 1 or len(words) > 2:
            return 'Invalid request'
        
        cmd, id = words[0], None
        if len(words) == 2:
            id = words[1]
            
        if cmd not in self.cmd_dicts:
            return 'Invalid request'
        
        return self.__process(cmd, id)

        # return self.cmd_dicts[request]()

# if __name__ == "__main__":
    # pass
    # controller = Controller()
    # print(controller.process('help'))
    # names, ids, threads = controller.list_apps()
    # for n, i, t in zip(names, ids, threads):
        # print(n, ' - ', i, ' - ', t)

    # names, ids, threads = controller.list_processes()
    # for n, i, t in zip(names, ids, threads):
    #     print(n, ' - ', i, ' - ', t)