import os
from .html_generator import html_msg

def __shutdown():
    msg = ''
    try:
        os.system(f'shutdown -s -t 8')
        msg = 'This device has been shutting down.'
        status = True
    except Exception as e:
        msg = 'There is an error when trying to shut down this device.'
        status = False
    return status, msg

def shutdown():
    status, msg = __shutdown()
    result = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }
    return result

def __restart():
    msg = ''
    try:
        os.system(f'shutdown -r -t 8')
        msg = 'This device has been restarting.'
        status = True
    except Exception as e:
        msg = 'There is an error when trying to restart this device.'
        status = False
    return status, msg

def restart():
    status, msg = __restart()

    result = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }

    return result