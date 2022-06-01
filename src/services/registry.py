import winreg, os, sys
import re
from .html_generator import html_table, html_msg

def __parse_registry(full_path):
    try:
        full_path = re.sub(r'/', r'\\', full_path)
        hive = re.sub(r'\\.*$', '', full_path)
        if not hive:
            raise ValueError('Invalid \'full_path\' param.')
        if len(hive) <= 4:
            if hive == 'HKLM':
                hive = 'HKEY_LOCAL_MACHINE'
            elif hive == 'HKCU':
                hive = 'HKEY_CURRENT_USER'
            elif hive == 'HKCR':
                hive = 'HKEY_CLASSES_ROOT'
            elif hive == 'HKU':
                hive = 'HKEY_USERS'
        reg_key = re.sub(r'^[A-Z_]*\\', '', full_path)
        reg_key = re.sub(r'\\[^\\]+$', '', reg_key)
        reg_value = re.sub(r'^.*\\', '', full_path)
        return hive, reg_key, reg_value
    except:
        return None, None, None

# def __parse_registry(full_path):
#     full_path = full_path.replace('/', '\\')
#     full_path = full_path.split('\\')
    
#     hive = full_path[0]
#     subkey = full_path[-1]
#     key = '\\'.join(full_path[1:-1])

#     if len(hive) <= 4:
#         if hive == 'HKLM':
#             hive = 'HKEY_LOCAL_MACHINE'
#         elif hive == 'HKCU':
#             hive = 'HKEY_CURRENT_USER'
#         elif hive == 'HKCR':
#             hive = 'HKEY_CLASSES_ROOT'
#         elif hive == 'HKU':
#             hive = 'HKEY_USERS'

#     if not hive or not key or not subkey:
#         return None, None, None

#     return hive, key, subkey

def __get(hive, key, subkey):
    value, _ = None, None
    try:
        kp = winreg.OpenKey(getattr(winreg, hive), key, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(kp, subkey) # (value, value type)
        winreg.CloseKey(kp)
    except:
        return False, f'Cannot get the value of registry.'
    
    return None, f'The value of registry is <span style="font-weight:bold">{value}</span>'

def get(full_path):
    hive, key, subkey = __parse_registry(full_path)

    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
        bold_all = True
    else:    
        status, msg = __get(hive, key, subkey)
        if status is None:
            bold_all = False
        else:
            bold_all = True
    response = {
        'html': html_msg(msg, status, bold_all),
        'data': None
    }
    return response

def __add_subkey(hive, key, subkey, value, dtype):
    try:
        winreg.CreateKey(getattr(winreg, hive), key + '\\' + subkey)
        kp = winreg.OpenKey(getattr(winreg, hive), key, 0 , winreg.KEY_WRITE)
        
        # k = winreg.OpenKeyEx(getattr(winreg, hive), key)
        # kp = winreg.CreateKey(k, value)

        if 'REG_BINARY' in dtype:
            if len(value) % 2 == 1:
                value = '0' + value # add padding
            value = int(value, 16).to_bytes(len(value) / 2, 'big')
        if 'REG_DWORD' in dtype:
            if len(value) > 8:
                value = value[:8]
            value = int(value, 16)
        if 'REG_QWORD' in dtype:
            if len(value) > 16:
                value = value[:16]
            value = int(value, 16)
            
        winreg.SetValueEx(kp, subkey, 0, getattr(winreg, dtype), value)
        if kp:
            winreg.CloseKey(kp)
    except:
        return False, f'Cannot create the registry subkey.'
    return True, f'The registry has been created.'

def add_subkey(fullpath, value, dtype):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:    
        status, msg = __add_subkey(hive, key, subkey, value, dtype)
    
    response = {
        'html': html_msg(msg, status, True),
        'data': None
    }

    return response

def __add_key(hive, key, subkey):
    try:
        # winreg.CreateKey(getattr(winreg, hive), key)
        print(key + '\\' + subkey)
        winreg.CreateKey(getattr(winreg, hive), key + '\\' + subkey)
    except:
        return False, 'Cannot create the registry key.'
    return True, 'The registry has been created.'
    
def add_key(fullpath):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:   
        print(hive, key, subkey, sep='\n')
        status, msg = __add_key(hive, key, subkey)
    
    response = {
        'html': html_msg(msg, status, True),
        'data': None
    }

    return response

def __modify_key(hive, key, subkey, value, dtype):
    try:
        winreg.CreateKey(getattr(winreg, hive), key)
        kp = winreg.OpenKey(getattr(winreg, hive), key, 0 , winreg.KEY_WRITE)
        
        if 'REG_BINARY' in dtype:
            if len(value) % 2 == 1:
                value = '0' + value # add padding
            value = int(value, 16).to_bytes(len(value) / 2, 'big')
        if 'REG_DWORD' in dtype:
            if len(value) > 8:
                value = value[:8]
            value = int(value, 16)
        if 'REG_QWORD' in dtype:
            if len(value) > 16:
                value = value[:16]
            value = int(value, 16)
            
        winreg.SetValueEx(kp, subkey, 0, getattr(winreg, dtype), value)
        winreg.CloseKey(kp)
    except:
        return False, f"Cannot modify the value of registry."
    return True, f"The value of registry has been modified."

def modify_key(fullpath, value, dtype):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:
        status, msg = __modify_key(hive, key, subkey, value, dtype)
    
    response = {
        'html': html_msg(msg, status, True),
        'data': None
    }
    
    return response

def __clear_value(hive, key, subkey):
    try:
        opened_key = winreg.OpenKey(getattr(winreg, hive), key, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(opened_key, subkey)
        winreg.CloseKey(opened_key)
    except:
        return False, f"Cannot clear the value of registry."
    return True, f"The value of registry has been cleared."

def clear_value(fullpath):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:
        status, msg = __clear_value(hive, key, subkey)
    
    response  = {
        'html': html_msg(msg, status, True),
        'data': None
    }
    return response

def __delete_key(hive, key, subkey):
    try:
        winreg.DeleteKey(getattr(winreg, hive), key + r'\\' + subkey)
    except:
        return False, f"Failed to delete the registry."
    
    return True, f"The registry was deleted."
        

def delete_key(fullpath):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:
        status, msg = __delete_key(hive, key, subkey)

    response = {
        'html': html_msg(msg, status, True),
        'data': None
    }
    return response

def __delete_subkey(hive, key, subkey):
    try:
        opened_key = winreg.OpenKey(getattr(winreg, hive), key, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(opened_key, subkey)
        winreg.CloseKey(opened_key)
    except:
        return False, 'Failed to delete the registry.'
    return True, 'The registry was deleted.'

def delete_subkey(fullpath):
    hive, key, subkey = __parse_registry(fullpath)
    if not hive or not key or not subkey:
        msg = 'Invalid registry path.'
        status = False
    else:
        status, msg = __delete_subkey(hive, key, subkey)

    response = {
        'html': html_msg(msg, status, True),
        'data': None
    }
    return response