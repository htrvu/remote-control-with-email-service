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
