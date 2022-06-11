import os
import shutil
from .html_generator import html_tree, html_msg

'''
    Private functions
'''
def __disk_list():
    disks = []
    for c in range(ord('A'), ord('Z') + 1):
        path = chr(c) + ":"
        if os.path.isdir(path):
            disks.append(path)
    return disks

def __listdir(path = None):
    if path is None:
        result = __disk_list()
    else:
        if os.path.exists(path):
            result = os.listdir(path)
        else:
            result = None
    return result

def __get_type(path):
    return 'file' if os.path.isfile(path) else 'directory'

def __copy(src, dst):
    type = __get_type(src)

    if not os.path.exists(src):
        return False,  f'The source {type} is not exist on this device.'

    try:
        if type == 'file':
            shutil.copyfile(src, dst)
        else:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        return True, f'The source {type} is copied successfully.'
    except:
        return False, f'The destination path might be wrong.'

def __cut(src, dst):
    type = __get_type(src)

    if not os.path.exists(src):
        return False,  f'The source {type} is not exist on this device.'

    try:
        shutil.move(src, dst)
        return True, f'The source {type} is moved successfully.'
    except:
        return False, f'The destination path might be wrong.'

def __delete(path):
    type = __get_type(path)

    if not os.path.exists(path):
        return False, f'The {type} you want to delete is not exist on this device.'

    try:
        if type == 'file':
            os.remove(path)
        else:
            shutil.rmtree(path)
        return True, f'The {type} is deleted successfuly.'
    except:
        return False, f'There is an error when deleting that {type}.'  


'''
    Public functions
'''

def show_tree(path = None):
    '''
        Return a dictionary with keys `html` and `data`, where `html` is the HTML directory tree (1-level) of `path`
    '''
    sub_dirs = __listdir(path)
    if sub_dirs is None:
        html = html_msg(f'The directory {path} is not exist on this device.', False)
    else:
        html = html_tree(path, sub_dirs)

    return {
        'html': html,
        'data': None
    }

def copy(src, dst):
    '''
        Copy the file or directory `src` to `dst`
        Return (status, msg), where `status` is a boolean and `msg` is a string
    '''
    status, msg = __copy(src, dst)
    return {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }

def cut(src, dst):
    '''
        Cut the file or directory `src` to `dst`
        Return (status, msg), where `status` is a boolean and `msg` is a string
    '''
    status, msg = __cut(src, dst)
    return {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }

def delete(path):
    '''
        Delete the file or directory `path`
        Return (status, msg), where `status` is a boolean and `msg` is a string
    '''
    status, msg = __delete(path)
    return {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }