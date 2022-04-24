import base64
import yaml
import email.message

def base64_decode(str):
    str = base64.b64decode(str)
    return str.decode('utf-8')

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

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def print_color(message, option = text_format.NORMAL, end = '\n'):
    print(f'{option[0]}{option[1]}{message} {text_format.UNDERLINE[0]}', end = end)
