import os, sys

app_location = os.getcwd()
checkpoint_file_name = 'checkpoint.yaml'
checkpoint_file_path = os.path.join(app_location, 'configs', checkpoint_file_name)

configs_file_name = 'app_configs.yaml'
configs_file_path = os.path.join(app_location, 'configs', configs_file_name)

screen_path = os.path.join(os.path.pardir(app_location), 'screen')
webcam_path = os.path.join(os.path.pardir(app_location), 'webcam')

app_configs = {
    'white_list': {},
    'auto_run': False
}