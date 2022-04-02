import base64

def base64_decode(str):
    str = base64.b64decode(str)
    return str.decode('utf-8')