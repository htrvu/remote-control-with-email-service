import os
import subprocess

def shutdown():
    try:
        os.system(f'shutdown -s')
    except Exception as e:
        return False

    return True


def restart():
    try:
        os.system(f'shutdown -r')
    except Exception as e:
        return False

    return True