import psutil
import os
from .html_generator import html_table, html_msg

def __process_df():
    result = {
        'status': 'OK',
        'type': 'single',
        'columns': ['No.', 'Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []
    cnt = 0
    for process in psutil.process_iter():
        try:
            cnt += 1
            data.append([cnt, process.name(), str(process.pid), process.num_threads()])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            cnt -= 1
            pass
    
    result['data'] = data

    return result


def get_processes():
    '''
        Return a dictionary with keys `html` and `data`, where `html` is the HTML table of running process list
    '''
    dataframe = __process_df()
    response = {
        'html': html_table(dataframe, format='center'),
        'data': None
    }
    return response


def __closing(id):
    '''
        Kill a running process with pID is `id` (`id` is a string)
        Return (status, msg), where `status` is a boolean and `msg` is a string
    ''' 
    # Get the id of running processes
    data = __process_df()
    exist = False
    for row in data['data']:
        if row[2] == id:
            exist = True
            break

    if not exist:
        return False, 'There is no process with pID ' + id + ' running on this device.'

    # Close the process
    try:
        p = psutil.Process(int(id))
        p.terminate()
        return True, 'The process with pID ' + id + ' is closed.'
    except:
        return False, 'There is an error when closing the process with pID ' + id + '.'

def close_process(id):
    '''
        Close a running process with pID is `id`. Return a dictionary with keys `html` and `data`, where `html` is the HTML of output message
    '''
    status, msg = __closing(id)
    response = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }
    return response
