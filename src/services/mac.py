from getmac import get_mac_address as gma
from .html_generator import html_msg

def __mac():
    msg = f'The MAC address of this device is <span style="font-weight: bold;">{gma()}</span>'
    return msg

def get_mac():
    '''
        Return a dictionary with keys `html` and `data`, where `html` is the HTML output message
    '''
    msg = __mac()
    response = {
        'html': html_msg(msg, status=None, bold_all=False),
        'data': None
    }
    return response
