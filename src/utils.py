import base64
import yaml
import re
import email.message
import datetime

import GlobalVariables

def base64_decode(str):
    str = base64.b64decode(str)
    return str.decode('utf-8')

def build_email_content(mail_from, mail_to, subject, content, format = 'html'):
    '''
        Build an email message with `mail_from`, `mail_to`, `subject` and `content`, where content is a 
        dictionary with keys `html` and `data`
    '''
    body = content['html']
    data = content['data']

    email_message = email.message.EmailMessage()
    email_message.add_header('To', ','.join(mail_to))
    email_message.add_header('From', mail_from)
    email_message.add_header('Subject', subject)
    email_message.add_header('X-Priority', '1')  # Urgency, 1 highest, 5 lowest
    email_message.set_content(body, format)

    if data is not None:
        # attach image to this mail
        email_message.add_attachment(data[1], maintype='image', subtype='png', filename=data[0])
        # # or
        # attach video to this mail
        email_message.add_attachment(data[1], maintype='video', subtype='avi', filename=data[0])

    return email_message

def mail_validate(mail):
    s = '^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(s, mail)

class text_format:
    HEADER = ['\033[95m', '']
    OKBLUE = ['\033[94m', '']
    OKCYAN = ['\033[96m', '']
    OKGREEN = ['\033[92m', '']
    WARNING = ['\033[93m', 'Warning: ']
    FAIL = ['\033[91m', 'Failed: ']
    ENDC = ['\033[0m', '']
    BOLD = ['\033[1m', '']
    UNDERLINE = ['\033[4m', '']
    NORMAL = ['','']
    DEBUG = ['\033[91m', '[DEBUG]: ']
    YELLOW = ['\033[93m', '']
    RED = ['\033[91m', '']
    EXCEPTION = ['\033[91m', '[Exception]: ']

def load_config(config_file = GlobalVariables.checkpoint_file_path):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def update_config_value(key, value, filename = GlobalVariables.checkpoint_file_path):
    yaml_dict = load_config(filename)
    
    yaml_dict[key] = value
    
    with open(filename, 'w') as f:
        yaml.dump(yaml_dict, f)

def print_color(message, option = text_format.NORMAL, end = '\n'):
    print(f'{option[0]}{option[1]}{message} {text_format.ENDC[0]}', end = end)

def print_indent(messages, level = 1, option = text_format.NORMAL, end = '\n'):
    if type(messages) == str:
        messages = messages.split('\n')
    
    for message in messages:
        print('\t' * level, end = '')
        print_color(message, option, end = end)
    
def date_format_str():
    return r"%Y-%m-%d"

def datetime_format_str():
    return r"%Y-%m-%d %H:%M:%S"

def date_today():
    return datetime.datetime.now().strftime(date_format_str())

def datetime_now_str():
    return datetime.datetime.now().strftime(datetime_format_str())

def time_in_range(start: datetime.datetime, end: datetime.datetime, x: datetime.datetime):
    
    start = start.timestamp()
    end = end.timestamp()
    x = x.timestamp()
    
    return start <= x <= end
