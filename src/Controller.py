import os, psutil, uuid
from getmac import get_mac_address as gma

class Controller:
    def __init__(self):
        pass

    def list_apps(self):
        cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
        ps_result = os.popen(cmd).read().split('\n')

        names, ids, threads = [], [], []

        for line in ps_result:
            if line.isspace() or len(line) == 0:
                continue

            arr = line.split(" ")

            # thread count
            threads.append(arr[-1])

            # id
            pos = len(arr) - 2
            for i in range(pos, -1, -1):
                if len(arr[i]) != 0:
                    ids.append(arr[i])
                    pos = i
                    break
            
            # name
            name = ''
            for i in range(0, pos):
                if len(arr[i]) != 0:
                    name = name + arr[i] + ' '
            name = name[:-1]
            names.append(name)
        
        return names, ids, threads


    def list_processes(self):
        names, ids, threads = ['Description'], ['Id'], ['ThreadCount']

        for process in psutil.process_iter():
            try:
                names.append(process.name())
                ids.append(process.pid)
                threads.append(process.num_threads())
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return names, ids, threads

# if __name__ == "__main__":
    # pass
    # controller = Controller()

    # names, ids, threads = controller.list_apps()
    # for n, i, t in zip(names, ids, threads):
        # print(n, ' - ', i, ' - ', t)

    # names, ids, threads = controller.list_processes()
    # for n, i, t in zip(names, ids, threads):
    #     print(n, ' - ', i, ' - ', t)