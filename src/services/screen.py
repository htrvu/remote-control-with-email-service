# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
from PIL import ImageGrab
import time
import os
import sys

sys.path.append('..')
import GlobalVariables

def screen_shot():
    im = ImageGrab.grab()
    try:
        os.mkdir(GlobalVariables.path_to_shots)
    except: pass
    filename = f'{GlobalVariables.path_to_shots}/{int(time.time())}.png'
    im.save(filename, 'PNG')
    img_data = open(filename, 'rb').read()
    msg = 'The screenshot is attached below.'
    return (os.path.basename(filename), img_data), msg

def screen_record():
    pass