import psutil
from .html_generator import html_table

def __process_df():
    result = {
        'status': 'OK',
        'columns': ['No.', 'Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []
    cnt = 0
    for process in psutil.process_iter():
        try:
            cnt += 1
            data.append([cnt, process.name(), process.pid, process.num_threads()])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            cnt -= 1
            pass
    
    result['data'] = data

    return result


def get_processes():
    '''
        Return the HTML table of running process list
    '''
    dataframe = __process_df()
    return html_table(dataframe, format='center')