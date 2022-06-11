from .html_generator import html_table

def __help_df():
    cmd_dict = {
        'HELP': {
            'HELP': 'Show the command list of this application.',
        },
        'EXPLORER': {
            'EXPLORER TREE <path>': 'Show the directory tree (1-level) of the <path>.',
            'EXPLORER COPY <source> <dest>': 'Copy the file or directory <source> to <dest>.',
            'EXPLORER MOVE <source> <dest>': 'Move the file or directory <source> to <dest>.',
            'EXPLORER DELETE <path>': 'Delete the file or directory <path>.',
        },
        'MAC': {
            'MAC get': 'Get the MAC address of the device.',
        },
        'APP': {
            'APP get': 'Get the list of running apps on the device.',
            'APP close <ID>': 'Close the running app with the given ID.',
        },
        'PROCESS': {
            'PROCESS get': 'Get the list of running processes on the device.',
            'PROCESS close <ID>': 'Close the running process with the given ID.',
        },
        'KEYLOGGER': {
            'KEYLOGGER get <duration>': 'Get the keylogger data of the device in <duration> seconds.',
        },
        'SCREEN': {
            'SCREEN get image': 'Get the screenshot of the device.',
            'SCREEN get video <duration>': 'Get the screen recording of the device in <duration> seconds.',
        },
        'WEBCAM': {
            'WEBCAM get image': 'Get the image from the webcam of the device.',
            'WEBCAM get video <duration>': 'Get the video from the webcam of the device in <duration> seconds.',
        },
        'PC': {
            'PC shutdown': 'Shut down the device.',
            'PC restart': 'Restart the device.',
        },
        'REGISTRY': {
            'REGISTRY get <hive>\<key>\<value name>': 'Get data and type of the registry value with name <value name> in <key> of root <hive>.',
            'REGISTRY add_key <hive>\<key>': 'Create new registry key <key> in root <hive>.',
            'REGISTRY add_value <hive>\<key>\<value name> <data> <type>': 'Create new registry value with name is <value name>, data is <data> and type is <type>, in <key> of root <hive>. The value of <type> must be REG_BINARY, REG_DWORD or REG_QWORD.',
            'REGISTRY modify <hive>\<key>\<value name> <data> <type>': 'Set the new data and type to registry value with name <value name> on <key> of root <hive>. The value of <type> must be REG_BINARY, REG_DWORD or REG_QWORD.',
            'REGISTRY delete_value <hive>\<key>\<value name>': 'Delete the registry value <value name> in <key> of root <hive>.',
            'REGISTRY delete_key <hive>\<key>': 'Delete the registry key <key> in root <hive>'
        }
    }

    result = {
        'status': 'OK',
        'type': 'group',
        'columns': ['Type', 'No.', 'Command', 'Description'],
        'data': []
    }

    cnt = 0
    for name, cmds in cmd_dict.items():
        group_cmds = []
        for cmd, desc in cmds.items():
            cnt += 1
            cmd = cmd.replace('<', '&lt;').replace('>', '&gt;')
            desc = desc.replace('<', '&lt;').replace('>', '&gt;')
            group_cmds.append([cnt, cmd, desc])
        result['data'].append([name, group_cmds])

    return result

def show_helps():
    '''
        Return the HTML table of command list
    '''
    dataframe = __help_df()
    note = '''
        <ul>
            <li>
            The commands can be written in uppercase like the following table or in any type of cases.
            <br>
            For example, APP, App or app are the same meaning.
            </li>
            <li>
            <span style="font-weight: bold;">&lt;duration&gt;</span> must be a non-negative integer and <span style="font-weight: bold;">&lt;path&gt;</span> must be put between 2 single (or double) quotes.
            <br>
            For example, &lt;path&gt; = \'C:/User/Some thing\' and &lt;path&gt; = "C:/User/Some thing" are valid.
            </li>
        </ul>
    '''
    return {
        'html': html_table(dataframe, note=note, format='left'),
        'data': None
    }
