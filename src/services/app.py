import os
from .html_generator import html_table

def __app_data():
    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    ps_result = os.popen(cmd).read().split('\n')
    
    result = {
        'status': 'OK',
        'columns': ['No.', 'Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []
    cnt = 0
    try:
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

            if len(name) == 0:
                continue

            cnt += 1
            data.append([cnt, name, id, thread_count])
    except:
        result['status'] = 'ERROR'

    result['data'] = data

    return result


def get_apps():
    '''
        Return the HTML table of running app list
    '''
    dataframe = __app_data()
    return html_table(dataframe, format='center')