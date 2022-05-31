import winreg, os, sys
# from html_generator import html_table, html_msg

def __get(hive, key, subkey):
    value, _ = None, None
    try:
        kp = winreg.OpenKey(getattr(winreg, hive), key, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(kp, subkey) # (value, value type)
        winreg.CloseKey(kp)
    except:
        return False, f'Cannot get value of {hive} {key} {subkey}'
    
    return True, f"Extract value of {hive} {key} {subkey} successfully!", value

def get(hive, key, subkey):
    status, msg, value = __get(hive, key, subkey)
    response = {
        'html': None, #html_msg(msg, status),
        'data': value
    }
    return response

def __new_key(hive, key, subkey):
    try:
        winreg.CreateKey(getattr(winreg, hive), key + r"\\" + subkey)
    except:
        return False, f'Cannot create {hive} {key}'
    return True, f'{hive} {key} created'

def new_key(hive, key, subkey):
    status, msg = __new_key(hive, key, subkey)
    response = {
        'html': None, #html_msg(msg, status),
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
            
        winreg.SetValueEx(kp, subkey[2], 0, getattr(winreg, dtype), value)
        winreg.CloseKey(kp)
    except:
        return False, f""
    return True, f""

def __drop_value(hive, key, subkey):
    try:
        opened_key = winreg.OpenKey(getattr(winreg, hive), key, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(opened_key, subkey)
        winreg.CloseKey(opened_key)
    except:
        return False, f""
    return True, f""

def drop_value(hive, key, subkey):
    status, message = __drop_value(hive, key, subkey)
    response  = {
        'html': None,
        'data': None
    }
    return response
    
def modify_key(hive, key, subkey, value, dtype):
    status, msg = __modify_key(hive, key, subkey, value, dtype)
    response = {
        'html': None, #html_msg(msg, status),
        'data': None
    }
    return response

def __drop_key(hive, key, subkey):
    
    try:
        winreg.DeleteKey(getattr(winreg, hive), key + r'\\' + subkey)
    except:
        return False, f"Failed to drop {hive} {key} {value}"
    
    return True, f"{hive} {key} {value} was deleted."
        

def drop_key(hive, key):
    status, msg = __drop_key(hive, key)
    response = {
        'html': None, #html_msg(msg, status),
        'data': None
    }
    return response