from getmac import get_mac_address as gma
from .html_generator import html_msg
def get_mac():
    '''
        Return a dictionary with keys `html` and `data`, where `html` is the HTML output message
    '''
    mac = 'The MAC address of this device is ' + gma()
    response = {
        'html': html_msg(mac),
        'data': None
    }
    return response
