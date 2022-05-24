import psutil

def get_process():
    result = {
        'status': 'OK',
        'column': ['Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []

    for process in psutil.process_iter():
        try:
            data.append([process.name(), process.pid, process.num_threads()])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    result['data'] = data

    return result