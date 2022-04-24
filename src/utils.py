import base64
import yaml
import email.message
import datetime
import GlobalVariables

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
    DEBUG = ['\033[91m', '[DEBUG]: ']

def load_config(config_file = GlobalVariables.checkpoint_file_path):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def html_table(data, column_names):
    html = "<table>"

    # column names
    html += '<tr>'
    for name in column_names:
        html += f'<th style="padding: 6px 8px; border: 1px solid #333; background-color: #4CAF50; color: white; font-weights: bold; text-align: center;">{name}</th>'
    html += '</tr>'

    # table data (rows)
    for row in data:
        html += '<tr>'
        for col in row:
            html += f'<td style="padding: 8px; border: 1px solid #333;">{col}</td>'
        html += '</tr>'

    html += '</table>'

    return html

def html_image(base64_data):
    html = f'<img src="data:image/png;base64,{base64_data}">'
    return html

def print_color(message, option = text_format.NORMAL, end = '\n'):
    print(f'{option[0]}{option[1]}{message} {text_format.ENDC[0]}', end = end)
    
def date_format_str():
    return r"%Y-%m-%d"

def datetime_format_str():
    return r"%Y-%m-%d %H:%M:%S"

def date_today():
    return datetime.datetime.now().strftime(date_format_str())

def datetime_now_str():
    return datetime.datetime.now().strftime(datetime_format_str())

def time_in_range(start: datetime, end: datetime, x: datetime, time_format = datetime_format_str()):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end