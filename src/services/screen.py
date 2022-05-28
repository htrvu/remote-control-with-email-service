# For screenshot image
from PIL import ImageGrab
import time
import os
import sys


# For screenshot record
from win32api import GetSystemMetrics
import cv2
import numpy as np

from .html_generator import html_msg


sys.path.append('..')
import GlobalVariables

def screen_shot():
    im = ImageGrab.grab()
    shots_path = GlobalVariables.screen_path + '/shots'
    try:
        if os.path.exists(GlobalVariables.screen_path):
            os.mkdir(GlobalVariables.screen_path)
        os.mkdir(shots_path)
    except: pass
    filename = f'{shots_path}/screen_{int(time.time())}.png'
    im.save(filename, 'PNG')

    msg = 'The screenshot is attached below.'
    response = {
        'html': html_msg(msg, True),
        'data': (os.path.basename(filename), open(filename, 'rb').read())
    }
    return response

def screen_record(elapse_time=10):
    SCREEN_SIZE = GetSystemMetrics(0), GetSystemMetrics(1) 
    fourcc = cv2.VideoWriter_fourcc(*"MP4V") # codec
    fps = 30

    records_path = GlobalVariables.screen_path + '/records'
    try:
        if os.path.exists(GlobalVariables.screen_path):
            os.mkdir(GlobalVariables.screen_path)
        os.mkdir(records_path)
    except: pass
    filename = f'{records_path}/screen_{int(time.time())}_{elapse_time}s.mp4'

    out = cv2.VideoWriter(filename, fourcc, fps, SCREEN_SIZE)
    for _ in range(fps * elapse_time):
        im = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()

    msg = 'The screen record is attached below.'
    response = {
        'html': html_msg(msg, True),
        'data': (os.path.basename(filename), open(filename, 'rb').read())
    }
    return response