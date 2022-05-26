import os
import subprocess

def shutdown(restart = False):
    try:
        os.system(f'shutdown {"-s" if not restart else "-r"}')
    except Exception as e:
        return False

    return True