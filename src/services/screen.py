# For screenshot image
from PIL import ImageGrab
import time
import os

# For screenshot record
from win32api import GetSystemMetrics
import cv2
import numpy as np

from .html_generator import html_msg

def __screen_shot():
    im = ImageGrab.grab()
    filename = f'./screen_{int(time.time())}.png'
    im.save(filename, 'PNG')

    return filename

def get_screen_shot():
    filename = __screen_shot()
    msg = 'The screenshot is attached below.'
    data = open(filename, 'rb').read()

    response = {
        'html': html_msg(msg, status=True, bold_all=True),
        'data': (os.path.basename(filename), data)
    }

    os.remove(filename)
    
    return response

def __screen_record(elapse_time=10):
    elapse_time = int(elapse_time)
    
    SCREEN_SIZE = GetSystemMetrics(0), GetSystemMetrics(1) 
    fourcc = cv2.VideoWriter_fourcc(*"mp4v") # codec
    fps = 30

    filename = f'./screen_{int(time.time())}_{elapse_time}s.mp4'

    out = cv2.VideoWriter(filename, fourcc, fps, SCREEN_SIZE)
    for _ in range(fps * elapse_time):
        im = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()

    return filename

def get_screen_record(elapse_time=10):
    filename = __screen_record(elapse_time)

    msg = 'The screen record is attached below.'
    data = open(filename, 'rb').read()

    response = {
        'html': html_msg(msg, status=True, bold_all=True),
        'data': (os.path.basename(filename), data)
    }

    os.remove(filename)

    return response