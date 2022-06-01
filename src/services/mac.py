from getmac import get_mac_address as gma
from .html_generator import html_msg
def get_mac():
    '''
        Return a dictionary with keys `html` and `data`, where `html` is the HTML output message
    '''
    mac = f'The MAC address of this device is <span style="font-weight: bold;">{gma()}</span>'
    response = {
        'html': html_msg(mac, status=None, bold_all=False),
        'data': None
    }
    return response
