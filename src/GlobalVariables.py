import os, sys

app_location = os.getcwd()
checkpoint_file_name = 'checkpoint.yaml'
checkpoint_file_path = os.path.join(app_location, 'configs', checkpoint_file_name)

screen_path = '../screen'
webcam_path = '../webcam'

app_configs = {
    'white_list': {},
    'autorun': False
}