import base64
import yaml
import re
import email.message
import subprocess

from win32com.client import Dispatch

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

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)
    
def save_config(config, file_Path):
    with open(file_Path, 'w') as fp:
        return yaml.dump(config, fp)

def update_config_value(key, value, filename):
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

def get_startup_path():
    cmd = '''echo %appdata%\Microsoft\Windows\Start Menu\Programs\Startup'''

    result = subprocess.check_output(cmd, shell=True)

    result = result.decode('utf-8')
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    result = result.replace('"', '')

    return result

def create_shortcut(path, target='', wDir='', icon=''):
    '''
    Example:
        path = os.path.join(desktop, "Media Player Classic.lnk")
        target = r"P:\Media\Media Player Classic\mplayerc.exe"
        wDir = r"P:\Media\Media Player Classic"
        icon = r"P:\Media\Media Player Classic\mplayerc.ico"
    '''
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    shortcut.save()