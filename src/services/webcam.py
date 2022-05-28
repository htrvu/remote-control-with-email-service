import cv2
import time
import sys
import os

from .html_generator import html_msg

sys.path.append('..')
import GlobalVariables

def webcam_record(elapse_time=10):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cap is None or not cap.isOpened():
        msg = 'Cannot capture from webcam. Make sure webcam is opened and try again later!'
        response = {
            'html': html_msg(msg, False),
            'data': None
        }
        return response

    fps = 30

    records_path = GlobalVariables.webcam_path + '/records'
    try:
        if not os.path.exists(GlobalVariables.webcam_path):
            os.mkdir(GlobalVariables.webcam_path)
        os.mkdir(records_path)
    except: pass
    filename = f'{records_path}/webcam_{int(time.time())}_{elapse_time}s.mp4'

    fourcc = cv2.VideoWriter_fourcc(*'MP4V') # codec

    width, height = int(cap.get(3)), int(cap.get(4))
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    for _ in range(elapse_time * fps):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything when finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    msg = 'The webcam record is attached below.'
    response = {
        'html': html_msg(msg, True),
        'data': (os.path.basename(filename), open(filename, 'rb').read())
    }
    return response

def webcam_shot():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cap is None or not cap.isOpened():
        msg = 'Cannot capture from webcam. Make sure webcam is opened and try again later!'
        response = {
            'html': html_msg(msg, False),
            'data': None
        }
        return response

    _, frame = cap.read()

    shots_path = GlobalVariables.webcam_path + '/shots'
    try:
        if not os.path.exists(GlobalVariables.webcam_path):
            os.mkdir(GlobalVariables.webcam_path)
        os.mkdir(shots_path)
    except: pass
    filename = f'{shots_path}/webcam_{int(time.time())}.png'
    cv2.imwrite(filename, frame)

    # Release everything when finished
    cap.release()
    cv2.destroyAllWindows()

    msg = 'The webcam capture is attached below.'
    response = {
        'html': html_msg(msg, True),
        'data': (os.path.basename(filename), open(filename, 'rb').read())
    }
    return response
