from request_handle import parse_request
from utils import *
from services.html_generator import html_msg, html_mail
from mail_service import MailService
from constants import REMOTE_MAIL

def respond(host_mail: MailService, mail):
    parse_result = parse_request(mail)
    
    response = None
    
    if not parse_result or 'function' not in parse_result:
        response = {
            'html': html_msg(parse_result['msg'], False),
            'data': None 
        }
    else:
        func = parse_result['function']
        params = parse_result['params']
        response = func(*params)
        
    content = {
        'html': html_mail(parse_result['command'], response['html']),
        'data': response['data']
    }

    mail_content = build_email_content(REMOTE_MAIL, [mail['sender']], f'Reply for request: {parse_result["command"]}', content = content)
    host_mail.send_mail(mail_content)
