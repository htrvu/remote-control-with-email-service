from request_handle import parse_request
from utils import *
from services.html_generator import html_msg

class Controller:
    def __init__(self):
        pass

    def respond(self, mail):
        func, param = parse_request(mail)
        
        if not func:
            response = {
                
            }
        
        response = func(*param)

        return response
