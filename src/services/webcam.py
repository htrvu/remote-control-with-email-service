import cv2
import time
import os

from .html_generator import html_msg

def __webcam_record(elapse_time=10):
    elapse_time = int(elapse_time)
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cap is None or not cap.isOpened():
        return None

    fps = 30
    filename = f'./webcam_{int(time.time())}_{elapse_time}s.mp4'

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec

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

    return filename

def get_webcam_record(elapse_time=10):
    filename = __webcam_record(elapse_time)
    if filename is None:
        msg = 'Cannot capture from webcam.'
        response = {
            'html': html_msg(msg, False, bold_all=True),
            'data': None
        }
        return response

    msg = 'The webcam record is attached below.'
    data = open(filename, 'rb').read()
    
    response = {
        'html': html_msg(msg, True, bold_all=True),
        'data': (os.path.basename(filename), data)
    }
    
    os.remove(filename)
    
    return response

def __webcam_shot():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cap is None or not cap.isOpened():
        return None

    _, frame = cap.read()
    filename = f'./webcam_{int(time.time())}.png'
    cv2.imwrite(filename, frame)

    # Release everything when finished
    cap.release()
    cv2.destroyAllWindows()

    return filename

def get_webcam_shot():
    filename = __webcam_shot()
    if filename is None:
        msg = 'Cannot capture from webcam.'
        response = {
            'html': html_msg(msg, False, bold_all=True),
            'data': None
        }
        return response

    msg = 'The webcam capture is attached below.'
    data = open(filename, 'rb').read()
    response = {
        'html': html_msg(msg, True, bold_all=True),
        'data': (os.path.basename(filename), data)
    }

    os.remove(filename)
    
    return response
