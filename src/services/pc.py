import os
from .html_generator import html_msg

def shutdown():
    msg = ''
    try:
        os.system(f'shutdown -s -t 5')
        msg = 'This device has been shutting down.'
        status = True
    except Exception as e:
        msg = 'There is an error when trying to shut down this device.'
        status = False

    result = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }

    return result


def restart():
    msg = ''
    try:
        os.system(f'shutdown -r -t 5')
        msg = 'This device has been restarting.'
        status = True
    except Exception as e:
        msg = 'There is an error when trying to restart this device.'
        status = False

    result = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }

    return result