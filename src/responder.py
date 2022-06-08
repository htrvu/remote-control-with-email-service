from request_handle import parse_request
from utils import *
from services.html_generator import html_msg, html_mail
from mail_service import MailService
from constants import REMOTE_MAIL
import app_logging as logging

def respond(host_mail: MailService, mail):
    key = random_key(10)
    
    logging.log(f'Thread {key}\tRequest from: {mail["sender"]}\tSubject: {mail["subject"]}')
    parse_result = parse_request(mail)
    logging.log(f'Thread {key}\tRequest parser message: {parse_result["msg"]}')
    
    response = None
    
    if parse_result['msg'] == 'Permission denied.':
        response = {
            'html': html_msg('You are not allowed to control this PC.', status = False, bold_all=True),
            'data': None
        }
    else:
        if not parse_result or 'function' not in parse_result:
            response = {
                'html': html_msg(parse_result['msg'], status=False, bold_all=True),
                'data': None 
            }
        else:
            func = parse_result['function']
            params = parse_result['params']
            logging.log(f'Thread {key}\tFunction {func}\tParams: {" ".join(params) if len(params) != 0 else "empty"}')
            try:
                response = func(*params)
            except:
                response = {
                    'html': html_msg('The format of arguments might be incorrect.', status=False, bold_all=True),
                    'data': None
                }
        
    content = {
        'html': html_mail(parse_result['command'], response['html']),
        'data': response['data']
    }
    
    mail_content = build_email_content(REMOTE_MAIL, [mail['sender']], f'Reply for request: {parse_result["command"]}', content = content)
    try:
        host_mail.send_mail(mail_content)
    except:
        logging.log(f'Thread {key}\tException raise when sending response to {mail["sender"]} ' + '(mail with attachment)' if content['data'] else '')
        return
    
    logging.log(f'Thread {key}\tThe response for request "{parse_result["command"]}" was send to {mail["sender"]} successfully')