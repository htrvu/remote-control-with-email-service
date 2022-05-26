from .html_generator import html_table

def __help_df():
    cmd_dict = {
        'HELP': 'Show the command list of this application.',
        'MAC get': 'Get the MAC address of the device.',
        'APP get': 'Get the list of running apps on the device.',
        'APP close <ID>': 'Close the running app with the given ID.',
        'PROCESS get': 'Get the list of running processes on the device.',
        'PROCESS close <ID>': 'Close the running process with the given ID.',
        'KEYLOGGER get <duration>': 'Get the keylogger data of the device in <duration> seconds. If <duration> is not given, the default value is 10 seconds.',
        'SCREEN get image': 'Get the screenshot of the device.',
        'SCREEN get video <duration>': 'Get the screen recording of the device in <duration> seconds. If <duration> is not given, the default value is 10 seconds.',
        'WEBCAM get image': 'Get the image from the webcam of the device.',
        'WEBCAM get video <duration>': 'Get the video from the webcam of the device in <duration> seconds. If <duration> is not given, the default value is 10 seconds.',
        'PC shutdown': 'Shut down the device.',
        'PC restart': 'Restart the device.',
        # registry ...
    }

    result = {
        'status': 'OK',
        'columns': ['No.', 'Command', 'Description'],
        'data': []
    }

    cnt = 0
    for cmd, desc in cmd_dict.items():
        cnt += 1
        cmd = cmd.replace('<', '&lt;').replace('>', '&gt;')
        desc = desc.replace('<', '&lt;').replace('>', '&gt;')
        result['data'].append([cnt, cmd, desc])

    return result

def show_helps():
    '''
        Return the HTML table of command list
    '''
    dataframe = __help_df()
    return html_table(dataframe, format='left')