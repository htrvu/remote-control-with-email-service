import os
from .html_generator import html_table, html_msg

def __app_data():
    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    ps_result = os.popen(cmd).read().split('\n')
    
    result = {
        'status': 'OK',
        'type': 'single',
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

def __closing(id):
    '''
        Close a running app with pID is `id` (`id` is a string)
        Return (status, msg), where `status` is a boolean and `msg` is a string
    ''' 
    # Get the id of running apps
    data = __app_data()
    exist = False
    for row in data['data']:
        if row[2] == id:
            exist = True
            break

    if not exist:
        return False, 'There is no app with pID ' + id + ' running on this device.'

    # Close the app
    try:
        cmd = 'powershell "gps | where {$_.mainWindowTitle} | where {$_.ID -eq ' + id + '} | select ID | kill"'
        ps_result = os.popen(cmd).read().split('\n')
        return True, 'The app with pID ' + id + ' is closed.'
    except:
        return False, 'There is an error when closing the app with pID ' + id + '.'

def close_app(id):
    '''
        Close a running app with pID is `id`
        Return status of closing process
    '''
    status, msg = __closing(id)
    return html_msg(msg, status)